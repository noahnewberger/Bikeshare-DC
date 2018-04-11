import pandas as pd
import util_functions as uf
import cabi_queries as cabi
import dockless_queries as dless
import secondary_queries as second
from psycopg2 import sql
import time


def cabi_agg_results(group_by_cols, drop_cols):
    # Aggregate the results from the CaBi Trip SQl query to different levels
    df = cabi_trips_df.drop(drop_cols, axis=1).groupby(group_by_cols).sum()
    return df


def cabi_cal_avgs(df):
    # For SQL efficiency, calculate averages from Cabi Trip data total fields
    calc_columns = [col for col in df.columns if "_tot" in col]
    for calc_column in calc_columns:
        avg_column = calc_column.replace('_tot', '_avg')
        df[avg_column] = df[calc_column] / df['cabi_trips']
    return df


def df_unstack(in_df, level):
    # Unstack Cabi Trips query results to make wide by descriptive field (ie Region and Member Type)
    df = in_df.unstack(level=level)
    df = pd.DataFrame(df.to_records()).set_index('date')
    df.columns = [hdr.replace("('", "").replace("', '", "_").replace("')", "") for hdr in df.columns]
    return df


def cabi_sum(sum_type, df):
    # Aggegrate sum type across regions
    sum_cols = [col for col in df if sum_type in col]
    series = df[sum_cols].sum(axis=1)
    return series


if __name__ == "__main__":
    # Connect to AWS
    uf.set_env_path()
    conn, cur = uf.aws_connect()

    # DOCKLESS: Trips
    dless_trips_df = dless.dockless_trips_by_operator(conn).set_index(['date'])
    dless_trips_df['dless_trips_all'] = dless_trips_df.sum(axis=1)

    # DOCKLESS: Total and Average Distance
    dless_trip_dist_tot_df = dless.dockless_trip_distance_total(conn).set_index(['date'])
    dless_trip_dist_tot_df['dless_tripdist_tot_all'] = dless_trip_dist_tot_df.sum(axis=1)
    dless_trip_dist_avg_df = dless.dockless_trip_distance_avg(conn).set_index(['date'])

    # DOCKLESS: Determine if dockless trips are geographic overlaps with CaBi stations
    dless_overlap_df = dless.dockless_overlap(conn)
    dless_overlap_df.set_index(['date', 'operator'], inplace=True)
    dless_overlap_df_unstack = df_unstack(in_df=dless_overlap_df, level=[-1])

    # DOCKLESS: Concat all Dockless Trip related dataframes
    dless_dfs = [dless_trips_df, dless_trip_dist_tot_df, dless_trip_dist_avg_df, dless_overlap_df_unstack]
    dless_df = pd.concat(dless_dfs, axis=1)

    # DOCKLESS: Calculate avg trip distances for all dockless trips
    dless_df['dless_tripdist_avg_all'] = dless_df['dless_tripdist_tot_all'] / dless_df['dless_trips_all']

    # Generate Dataframe of Cabi Trip Stats by Region and Member
    cabi_trips_df = cabi.cabi_trips_by_region_member(conn)

    # Copy Dataframe for further calculation by Region and Member and set index
    by_region_member_df = cabi_trips_df.set_index(['date', 'region_to_region', 'member_type'])
    # Calculate Avgs for Duration, Cost and Distance
    by_region_member_df = cabi_cal_avgs(df=by_region_member_df)
    # Unstack by Region and Member Type
    by_region_member_df_unstack = df_unstack(in_df=by_region_member_df, level=[-2, -1])

    # Generate Dataframe of Cabi Trip Stats by Region only
    by_region_df = cabi_agg_results(group_by_cols=['date', 'region_to_region'], drop_cols=['member_type'])
    # Calculate Avgs for Duration, Cost and Distance
    by_region_df = cabi_cal_avgs(df=by_region_df)
    # Unstack by Region
    by_region_df_unstack = df_unstack(in_df=by_region_df, level=[-1])

    # Generate Dataframe of Cabi Trip Stats by Member Type only
    by_mem_type_df = cabi_agg_results(group_by_cols=['date', 'member_type'], drop_cols=['region_to_region'])
    # Calculate Avgs for Duration, Cost and Distance
    by_mem_type_df = cabi_cal_avgs(df=by_mem_type_df)
    # Unstack by Member Type
    by_mem_type_unstack = df_unstack(in_df=by_mem_type_df, level=[-1])

    # Generate Dataframe of Cabi Trip Stats Total
    by_tot_df = cabi_agg_results(group_by_cols=['date'], drop_cols=['region_to_region', 'member_type'])
    # Calculate Avgs for Duration, Cost and Distance
    by_tot_df = cabi_cal_avgs(df=by_tot_df)

    # CaBi Bike Available
    cabi_bikes_df = cabi.cabi_bikes_available(conn).set_index(['date'])

    # CaBi Stations Available
    cabi_stations_df = cabi.cabi_stations_available(conn)
    # Unstack Stations data by region
    cabi_stations_unstack = df_unstack(in_df=cabi_stations_df.set_index(['date', 'region_code']), level=[-1])
    # Calculate total station and docks
    cabi_stations_unstack['cabi_stations_tot'] = cabi_sum(sum_type='stations', df=cabi_stations_unstack)
    cabi_stations_unstack['cabi_docks_tot'] = cabi_sum(sum_type='docks', df=cabi_stations_unstack)

    # CaBi Outage History
    cabi_outhist_df = cabi.cabi_outage_history(conn)
    # Unstack Stations data by region and status type (full or empty)
    cabi_outhist_unstack = df_unstack(in_df=cabi_outhist_df.set_index(['date', 'status', 'region_code']), level=[-2, -1])
    # Calculate total empty and full
    cabi_outhist_unstack['cabi_dur_empty_tot'] = cabi_sum(sum_type='empty', df=cabi_outhist_unstack)
    cabi_outhist_unstack['cabi_dur_full_tot'] = cabi_sum(sum_type='full', df=cabi_outhist_unstack)

    # Merge all CaBI DFs together
    cabi_dfs = [by_tot_df,
                by_mem_type_unstack,
                by_region_df_unstack,
                by_region_member_df_unstack,
                cabi_bikes_df,
                cabi_stations_unstack,
                cabi_outhist_unstack]

    cabi_df = pd.concat(cabi_dfs, axis=1)
    # Calculate CaBi Syste Utilization Rate
    cabi_df['cabi_util_rate'] = cabi_df['cabi_trips'] / cabi_df['cabi_bikes_avail']

    # Gather all Secondary Data sources
    dark_sky_df = second.dark_sky(conn).set_index('date')

    # Merge all DFs together
    df_final = dark_sky_df.merge(cabi_df, how='left', left_index=True, right_index=True)
    df_final = df_final.merge(dless_df, how='left', left_index=True, right_index=True)
    # Define numeric columns for create table statement prior to resetting index to bring back date field
    numeric_cols = ", ".join([col + " numeric" for col in df_final.columns])
    df_final.fillna(0, inplace=True)
    df_final.reset_index(inplace=True)

    # Output final dataframe
    outname = "final_db_pipe_delimited"
    df_final.to_csv(outname + ".csv", index=False, sep='|')

    # CREATE TABLE on AWS
    TIMESTR = time.strftime("%Y%m%d_%H%M%S")
    db_name = "final_db_" + TIMESTR
    cur.execute(sql.SQL("CREATE TABLE {0}(date date PRIMARY KEY," + numeric_cols + ")").format(sql.Identifier(db_name)))

    # Load to Database
    uf.aws_load(outname, db_name, cur)
    # Commit changes to database
    conn.commit()
