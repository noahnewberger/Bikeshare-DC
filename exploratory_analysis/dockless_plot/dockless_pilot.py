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
