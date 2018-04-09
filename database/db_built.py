import pandas as pd
import util_functions as uf
import sql_queries as sql


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


def cabi_unstack(in_df, level):
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

    # CaBi Stations Available
    cabi_stations_df = sql.cabi_stations_available(conn)
    # Unstack Stations data by region
    cabi_stations_unstack = cabi_unstack(in_df=cabi_stations_df.set_index(['date', 'region_code']), level=[-1])
    # Calculate total station and docks
    cabi_stations_unstack['cabi_stations_tot'] = cabi_sum(sum_type='stations', df=cabi_stations_unstack)
    cabi_stations_unstack['cabi_docks_tot'] = cabi_sum(sum_type='docks', df=cabi_stations_unstack)

    # Generate Dataframe of Cabi Trip Stats by Region and Member
    cabi_trips_df = sql.cabi_trips_by_region_member(conn)

    # Copy Dataframe for further calculation by Region and Member and set index
    by_region_member_df = cabi_trips_df.set_index(['date', 'region_to_region', 'member_type'])
    # Calculate Avgs for Duration, Cost and Distance
    by_region_member_df = cabi_cal_avgs(df=by_region_member_df)
    # Unstack by Region and Member Type
    by_region_member_df_unstack = cabi_unstack(in_df=by_region_member_df, level=[-2, -1])

    # Generate Dataframe of Cabi Trip Stats by Region only
    by_region_df = cabi_agg_results(group_by_cols=['date', 'region_to_region'], drop_cols=['member_type'])
    # Calculate Avgs for Duration, Cost and Distance
    by_region_df = cabi_cal_avgs(df=by_region_df)
    # Unstack by Region
    by_region_df_unstack = cabi_unstack(in_df=by_region_df, level=[-1])

    # Generate Dataframe of Cabi Trip Stats by Member Type only
    by_mem_type_df = cabi_agg_results(group_by_cols=['date', 'member_type'], drop_cols=['region_to_region'])
    # Calculate Avgs for Duration, Cost and Distance
    by_mem_type_df = cabi_cal_avgs(df=by_mem_type_df)
    # Unstack by Member Type
    by_mem_type_unstack = cabi_unstack(in_df=by_mem_type_df, level=[-1])

    # Generate Dataframe of Cabi Trip Stats Total
    by_tot_df = cabi_agg_results(group_by_cols=['date'], drop_cols=['region_to_region', 'member_type'])
    # Calculate Avgs for Duration, Cost and Distance
    by_tot_df = cabi_cal_avgs(df=by_tot_df)

    # CaBi Bike Available
    cabi_bikes_df = sql.cabi_bikes_available(conn).set_index(['date'])

    # CaBi Outage History
    cabi_outhist_df = sql.cabi_outage_history(conn)
    # Unstack Stations data by region and status type (full or empty)
    cabi_outhist_unstack = cabi_unstack(in_df=cabi_outhist_df.set_index(['date', 'status', 'region_code']), level=[-2, -1])
    # Calculate total empty and full
    cabi_outhist_unstack['cabi_dur_empty_tot'] = cabi_sum(sum_type='empty', df=cabi_outhist_unstack)
    cabi_outhist_unstack['cabi_dur_full_tot'] = cabi_sum(sum_type='full', df=cabi_outhist_unstack)

    # Merge all DFs together
    dfs = [by_tot_df, by_mem_type_unstack, by_region_df_unstack, by_region_member_df_unstack, cabi_bikes_df, cabi_stations_unstack, cabi_outhist_unstack]
    df_final = pd.concat(dfs, axis=1)
    # Calculate CaBi Syste Utilization Rate
    df_final['cabi_util_rate'] = df_final['cabi_trips'] / df_final['cabi_bikes_avail']

    # Define numeric columns for create table statement prior to resetting index to bring back date field
    numeric_cols = ", ".join([col + " numeric" for col in df_final.columns])
    df_final.reset_index(inplace=True)

    # Output final dataframe
    outname = "final_db_pipe_delimited"
    df_final.to_csv(outname + ".csv", index=False, sep='|')

    # CREATE TABLE on AWS
    cur.execute("""
                DROP TABLE IF EXISTS final_db;
                CREATE TABLE final_db(
                date date PRIMARY KEY,""" +
                numeric_cols +
                """)"""
                )

    # Load to Database
    uf.aws_load(outname, "final_db", cur)
    # Commit changes to database
    conn.commit()
