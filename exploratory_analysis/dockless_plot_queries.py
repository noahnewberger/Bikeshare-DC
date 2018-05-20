import pandas as pd
import numpy as np
import util_functions as uf


if __name__ == "__main__":
    # Connect to AWS
    uf.set_env_path()
    conn, cur = uf.aws_connect()

    '''Single Trips as % of all CaBi passes (not memberships) purchased monthly
        [[PLOT]]
    '''
    df = pd.read_sql("""select
                        month,
                        (single_trip_pass_purch/(multi_day_pass_purch + single_day_pass_purch + single_trip_pass_purch)) as single_pass_perc
                        from cabi_membership
                        where single_trip_pass_purch>0;
                     """, con=conn)
    print(df.tail(20))
    import sys
    sys.exit()
    '''
    Notes for Noah:
        * The goal here is show that the vast majority of casual rides would be impacted by increase in dockless demand
          as our ML will hopefully prove out.
        * This is just a first cut, but wanted to give all the relevant variables and table names.
    '''
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
                              AND userid != '0'
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

    '''
    Distribution of Dockless Trips by Hour
    [[PLOT]]
    '''

    # TBD: need to make timetable of Metro Peak Hours

    '''
    Daily Active Users (Dockless) vs CaBi Members
    [[PLOT]]
    '''
    df = pd.read_sql("""select distinct
                        date,
                        /* Active Users for Individual Dockless Operators*/
                        dless_users_jump,
                        dless_users_lime,
                        dless_users_mobike,
                        dless_users_ofo,
                        dless_users_spin,
                        /* Total Active Users for Dockless Operators*/
                        (dless_users_jump +
                         dless_users_lime +
                         dless_users_mobike +
                         dless_users_ofo +
                         dless_users_spin) as dless_users_total,
                        /* Total Active Users */
                        (cabi_active_members_day_key +
                        cabi_active_members_monthly +
                        cabi_active_members_annual) as cabi_active_members_total
                        from final_db
                        where dless_trips_all > 0
                        """, con=conn)
    print(df.tail())

    '''
    Notes for Noah:
        * Mobike was kept in here in case we get better userids'
        * Don't have active users for Jump for February will potentially need to get some DDOT
        * This should be done at the daily basis as Lime, Spin and Mobike figures change daily
    '''

    '''
    Geographic Overlap by Operator Over Time
    [[PLOT]]
    '''
    df = pd.read_sql("""select distinct
                        date,
                        /* % of trips that Start within quarter mile of CaBi Station*/
                        dless_geo_start_lime,
                        dless_geo_start_mobike,
                        dless_geo_start_ofo,
                        dless_geo_start_spin,
                        /* % of trips that End within quarter mile of CaBi Station*/
                        dless_geo_end_lime,
                        dless_geo_end_mobike,
                        dless_geo_end_ofo,
                        dless_geo_end_spin
                        from final_db
                        where dless_trips_all > 0
                        """, con=conn)
    print(df.tail())

    '''
    Notes for Noah:
        * Jump purposefully removed here as it's highly unlikely we'll get better geocoordinate data for them
    '''

    '''
    Capacity Overlap by Operator Over Time
    [[PLOT]]
    '''
    df = pd.read_sql("""select distinct
                        date,
                        /* % of trips that Start within quarter mile of CaBi Station when said Station is Empty*/
                        dless_cap_start_lime::float,
                        dless_cap_start_mobike,
                        dless_cap_start_ofo,
                        dless_cap_start_spin
                        from final_db
                        where dless_trips_all > 0
                        """, con=conn)
    print(df.tail())
    '''
    Notes for Noah:
        * Jump purposefully removed here as it's highly unlikely we'll get better geocoordinate data for them
        * We only care about dockless starts because where a person ends a dockless trip has no bearing on CaBi station Capacity
        * IMPORTANT: Hold off on workong on this for now.  There is an error in the way I calculated these fields
          I need to re-work a bunch of stuff, but we should decide if it's worthwhile first
    '''
    '''
    % of total trips by Operator per ANC vs CaBi - TWO plots trip starts and trip ends
    [[PLOT]]
    '''
    df = pd.read_sql("""SELECT DISTINCT
                            start_anc.start_anc,
                            start_anc_trips,
                            end_anc_trips,
                            dless_total_trips,
                            start_anc_trips/dless_total_trips::float as dless_start_perc,
                            end_anc_trips/dless_total_trips::float as dless_end_perc,
                            cabi_trips_start,
                            cabi_trips_end,
                            cabi_total_trips,
                            cabi_trips_start/cabi_total_trips::float as cabi_start_perc,
                            cabi_trips_end/cabi_total_trips::float as cabi_end_perc
                            FROM
                            /* Count of dockless start anc trips*/
                            (SELECT DISTINCT
                            start_anc,
                            count(*) as start_anc_trips
                            FROM dockless_trips_geo
                            WHERE operatorclean != 'jump' and start_anc is not null
                            group by 1) as start_anc
                            /* Count of dockless end anc trips*/
                            LEFT JOIN
                            (SELECT DISTINCT
                            end_anc,
                            count(*) as end_anc_trips
                            FROM dockless_trips_geo
                            WHERE operatorclean != 'jump' and end_anc is not null
                            group by 1) as end_anc
                            ON start_anc.start_anc = end_anc.end_anc
                            /* Count of Total Dockless Trips*/
                            LEFT JOIN
                            (SELECT DISTINCT
                             count(*) as dless_total_trips
                             FROM dockless_trips_geo
                             where operatorclean != 'jump')  as tot
                             on start_anc.start_anc = start_anc.start_anc
                             /* Count of Total DC to DC CaBi Trips during dockless pilot*/
                             LEFT JOIN
                             (SELECT DISTINCT
                              sum(cabi_trips_wdc_to_wdc) as cabi_total_trips
                              FROM final_db
                              where dless_trips_all > 0) as cabi_tot
                              on start_anc.start_anc = start_anc.start_anc
                            /* Count CaBi trips starts*/
                            LEFT JOIN
                                (select distinct
                                start_anc,
                                count(*) as cabi_trips_start
                                from
                                (select * from
                                cabi_trips
                                where start_date::date >= '09-09-2017' and start_date::date <= '02-28-2018') as cabi_trips
                                /*keep only dc to dc cabi trips*/
                                inner join
                                (select distinct
                                 start_short_name,
                                 end_short_name,
                                 start_anc,
                                 end_anc
                                 from cabi_stations_geo_temp
                                 where start_anc != '' and end_anc != '') as cabi_geo
                                on cabi_trips.start_station = cabi_geo.start_short_name and cabi_trips.end_station = cabi_geo.end_short_name
                                group by 1) as cabi_starts
                            ON start_anc.start_anc = cabi_starts.start_anc
                            /* Count CaBi trip ends*/
                            LEFT JOIN
                                (select distinct
                                end_anc,
                                count(*) as cabi_trips_end
                                from
                                (select * from
                                cabi_trips
                                where start_date::date >= '09-09-2017' and start_date::date <= '02-28-2018') as cabi_trips
                                /*keep only dc to dc cabi trips*/
                                inner join
                                (select distinct
                                 start_short_name,
                                 end_short_name,
                                 start_anc,
                                 end_anc
                                 from cabi_stations_geo_temp
                                 where start_anc != '' and end_anc != '') as cabi_geo
                                on cabi_trips.start_station = cabi_geo.start_short_name and cabi_trips.end_station = cabi_geo.end_short_name
                                group by 1) as cabi_ends
                            ON start_anc.start_anc = cabi_ends.end_anc
                        """, con=conn)
    print(df.tail())

    '''
    Notes for Noah:
        * Jump purposefully removed here as it's highly unlikely we'll get better geocoordinate data for them
        * We'll need to adjust the cabi_trip data manually to line up with pilot depending on what data we get
        * This query takes about a minute to run, be patient

    '''
    import sys
    sys.exit()
