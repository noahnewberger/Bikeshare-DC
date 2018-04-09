import pandas as pd


def cabi_trips_by_region_member(conn):
    # CaBi Trips by Member Type and Region (joined on)
    df = pd.read_sql("""SELECT DISTINCT
                        trips.start_date::date as date,
                        concat_ws('_to_', start_st.region_code::text, end_st.region_code::text) AS region_to_region,
                        trips.member_type,
                        /*Total Trips*/
                        COUNT(*) as cabi_trips,
                        /* Aggregate duration in seconds*/
                        SUM(EXTRACT('epoch' FROM (trips.end_date - trips.start_date))) as cabi_trip_dur_tot,
                        /* Calculate distance in meters*/
                        SUM(ST_DistanceSpheroid(ST_SetSRID(st_makepoint(start_st.lon, start_st.lat),4326),
                            ST_SetSRID(st_makepoint(end_st.lon, end_st.lat),4326), 'SPHEROID["WGS 84",6378137,298.257223563]')) as cabi_trip_dist_tot,
                        /*Calculate Trip Cost*/
                        SUM(CASE WHEN trips.member_type = 'Member' THEN price.member_cost
                             ELSE price.casual_cost + 2 END) as cabi_trip_cost_tot
                        from cabi_trips as trips
                        /* Join region to start station*/
                        LEFT JOIN
                        (SELECT distinct short_name, lat, lon, cabi_system.code AS region_code
                              FROM cabi_stations_temp
                              LEFT JOIN cabi_system
                              ON cabi_stations_temp.region_id = cabi_system.region_id) as start_st
                        ON trips.start_station = start_st.short_name
                        /* Join region to end station*/
                        LEFT JOIN
                        (SELECT distinct short_name, lat, lon, cabi_system.code AS region_code
                              FROM cabi_stations_temp
                              LEFT JOIN cabi_system
                              ON cabi_stations_temp.region_id = cabi_system.region_id) as end_st
                        ON trips.end_station = end_st.short_name
                        /*Join CaBi Price table*/
                        LEFT JOIN cabi_price as price
                        ON EXTRACT('epoch' FROM (trips.end_date - trips.start_date)) BETWEEN price.min_seconds AND price.max_seconds
                        /*TEMPORARY where statement for efficient testing*/
                        WHERE trips.start_date::date >= '2017-09-20'
                        GROUP by 1, 2, 3;
                 """, con=conn)
    return df


def cabi_bikes_available(conn):
    # Calculate Cabi Bike Available based on bike min and max usage date, will ultimately be replaced by true CaBi Bike History
    df = pd.read_sql("""SELECT ds.weather_date as date,
                          COUNT(DISTINCT cabi_bikes.bike_number) as cabi_bikes_avail
                          FROM dark_sky_raw as ds
                          LEFT JOIN
                            (SELECT DISTINCT bike_number,
                            MIN(start_date::timestamp::date) AS bike_min_date,
                              (date_trunc('month', MAX(start_date)) + interval '1 month')::date AS bike_max_date

                            FROM cabi_trips
                            GROUP BY 1) as cabi_bikes
                          ON ds.weather_date BETWEEN cabi_bikes.bike_min_date AND cabi_bikes.bike_max_date
                          /*TEMPORARY where statement for efficient testing*/
                          WHERE ds.weather_date >= '2017-09-20'
                          GROUP BY 1;
                     """, con=conn)
    return df


def cabi_stations_available(conn):
    # Calculate Cabi stations Available based on station min and max usage date, will ultimately be replaced by true CaBi Station History
    df = pd.read_sql("""SELECT ds.weather_date as date,
                        cabi_stations.region_code,
                        COUNT(DISTINCT cabi_stations.station) as cabi_stations,
                        SUM(cabi_stations.docks) as cabi_docks
                        FROM dark_sky_raw as ds
                        LEFT JOIN
                        ((select distinct
                          region_code,
                          station,
                          MIN(station_min_date) AS station_min_date,
                          MAX(station_max_date) AS station_max_date,
                          SUM(capacity) as docks
                          from
                          /* Stack start and end station history from cabi trips*/
                          (((SELECT DISTINCT
                            start_station as station,
                            MIN(start_date::timestamp::date) AS station_min_date,
                            (date_trunc('month', MAX(start_date)) + interval '1 month')::date AS station_max_date
                            FROM cabi_trips
                            GROUP BY 1)
                          union
                          (SELECT DISTINCT
                            end_station as station,
                            MIN(start_date::timestamp::date) AS station_min_date,
                            (date_trunc('month', MAX(start_date)) + interval '1 month')::date AS station_max_date
                            FROM cabi_trips
                            GROUP BY 1)) as stations
                          /* Bring on Region Code from cabi station and system API data*/
                          LEFT JOIN (SELECT distinct
                                     short_name,
                                     capacity,
                                     cabi_system.code AS region_code
                                     FROM cabi_stations_temp
                                     LEFT JOIN cabi_system
                                     ON cabi_stations_temp.region_id = cabi_system.region_id) as region_code
                                     ON stations.station = region_code.short_name
                                     )
                          GROUP BY 1, 2
                          ORDER BY 1, 2)) as cabi_stations
                        ON ds.weather_date BETWEEN cabi_stations.station_min_date AND cabi_stations.station_max_date
                        /*TEMPORARY where statement for efficient testing*/
                        WHERE ds.weather_date >= '2017-09-20'
                        GROUP BY 1, 2;
                        """, con=conn)
    return df


def cabi_outage_history(conn):
    # Calculate empty and full duration at Cabi stations by CaBi region
    df = pd.read_sql("""SELECT
                        out_hist.start_time::date as date,
                        out_hist.status,
                        region_code.region_code,
                        SUM(EXTRACT('epoch' FROM (out_hist.end_time - out_hist.start_time))) as cabi_dur
                        FROM cabi_out_hist as out_hist
                        /* Bring on Region Code from cabi station and system API data*/
                        LEFT JOIN (SELECT distinct
                              short_name,
                              cabi_system.code AS region_code
                              FROM cabi_stations_temp
                                    LEFT JOIN cabi_system
                                    ON cabi_stations_temp.region_id = cabi_system.region_id) as region_code
                        ON out_hist.terminal_number = region_code.short_name
                        /*TEMPORARY where statement for efficient testing*/
                        WHERE out_hist.start_time::date >= '2017-09-20'
                        GROUP BY 1, 2, 3;
                        """, con=conn)
    return df
