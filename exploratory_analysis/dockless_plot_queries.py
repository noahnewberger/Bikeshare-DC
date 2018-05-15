import pandas as pd
import numpy as np
import util_functions as uf


if __name__ == "__main__":
    # Connect to AWS
    uf.set_env_path()
    conn, cur = uf.aws_connect()
    '''
    Percentage of Total Rides: Dockless vs. CaBi (Total and CaBI)
    [[PLOT]]
    '''
    df = pd.read_sql("""select distinct
                        date,
                        /*Get Daily Percentage by taking daily totals and dividing by pilot totals*/
                        (cabi_trips_wdc_to_wdc/cabi_trips_wdc_to_wdc_pilot) as cabi_total_perc,
                        (cabi_trips_wdc_to_wdc_casual/cabi_trips_wdc_to_wdc_casual_pilot) as cabi_casual_perc,
                        (dless_trips_all/dless_trips_all_pilot) as dless_total_perc
                        from final_db as db
                        left join
                        /*Aggregate Trips for the entire Pilot for CaBi and Dockless Totals*/
                        (select
                        sum(cabi_trips_wdc_to_wdc) as cabi_trips_wdc_to_wdc_pilot,
                        sum(cabi_trips_wdc_to_wdc_casual) as cabi_trips_wdc_to_wdc_casual_pilot,
                        sum(dless_trips_all) as dless_trips_all_pilot
                        from final_db
                        where dless_trips_all > 0) as tot
                        on db.date = db.date
                        where dless_trips_all > 0;
                     """, con=conn)
    print(df.head())
    
    '''
    Notes for Noah:
    * Should be two plots Cabi Total vs Dockless Total and Cabi Casual Vs Dockless Total
    * X axis should be "date", either figure out how only show every n x-tick or hide x axis tick label and
      describe x axis in overall label such as "Day in Dockless Pilot (9/9/2017 - 2/28/2018).
    '''

    '''Total Dockless Trips (Aggregate) by day of pilot vs Total CaBi Trips by day of pilot (Total and Casual)
    [[PLOT]]
    '''
    df = pd.read_sql("""select distinct
                        date,
                        sum(cabi_trips_wdc_to_wdc) as cabi_trips_wdc_to_wdc_pilot,
                        sum(cabi_trips_wdc_to_wdc_casual) as cabi_trips_wdc_to_wdc_casual_pilot,
                        sum(dless_trips_all) as dless_trips_all_pilot
                        from final_db
                        where dless_trips_all > 0
                        group by 1;
                     """, con=conn)
    print(df.head())

    '''
    Notes for Noah:
    * This was originally monthly, but might be more interesting at the daily level.daily and will match plot above
    * X axis should be "date", either figure out how only show every n x-tick or hide x axis tick label and
      describe x axis in overall label such as "Day in Dockless Pilot (9/9/2017 - 2/28/2018).
    '''

    '''
    Frequency of Trips per user (Pareto Chart) for each dockless operator (except for Mobike)
    [[PLOT]]
    '''
    df = pd.read_sql("""select distinct
                        user_freqs.operatorclean,
                        user_freqs.user_trips,
                        count(*) as freq_user_trips
                        from
                        ((select distinct
                        operatorclean,
                        userid,
                        count(*) as user_trips
                        from dockless_trips
                        where operatorclean in ('mobike', 'lime', 'spin')
                        group by 1, 2
                        order by operatorclean, count(*))
                        union
                        /*ofo users*/
                        (select distinct
                        'ofo' as operatorclean,
                        userid,
                        sum(trips) as user_trips
                        from ofo_users
                        group by 1, 2
                        order by operatorclean, sum(trips))
                        union
                        /*jump users*/
                        (select distinct
                        'jump' as operatorclean,
                        userid,
                        sum(trips) as user_trips
                        from jump_users
                        group by 1, 2
                        order by operatorclean, sum(trips))) as user_freqs
                        group by 1, 2
                        order by 1, 2;
                     """, con=conn)

    # Initialize Excel Instance
    writer = pd.ExcelWriter('Dockless_User_Frequency_Analysis.xlsx')

    for operator in df['operatorclean'].drop_duplicates().tolist():
        operator_df = df[df['operatorclean'] == operator].copy()

        # Calculate Cumulative Sum and Perc
        operator_df['cumulative_sum'] = operator_df['freq_user_trips'].cumsum()
        operator_df['cumulative_percent'] = operator_df['cumulative_sum'] / operator_df['freq_user_trips'].sum()

        # Output to Excel
        operator_df.to_excel(writer, sheet_name=operator, index=False)
    writer.save()
    print(df.head())
    '''
    Notes for Noah:
    * This plot will be done in Excel, no need to do anything with these results
    * Please keep this query since it  will be leveraged for next plot
    '''

    '''
    Stacked Bar Chart showing % of trips taken by users who took 5 trips or less vs greater than 5 trips.
    One bar for each operator for the entire pilot (except Mobike)
    [[PLOT]]'''
    df['le_5'] = np.where(df['user_trips'] <= 5, 'LEQ 5 Trips', "GT 5 Trips")
    le_5_df = df.groupby(['operatorclean', 'le_5'])['freq_user_trips'].sum()
    print(le_5_df)
    '''
    Notes for Noah:
    * Use "le_5_df" for the plot which has a multi-index of "operatorclean" and "le_5"
    * Mobike was kept in here in case we get better userids'
    '''
    import sys
    sys.exit()
