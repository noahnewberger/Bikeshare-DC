import pandas as pd


def dockless_trips_by_operator(conn):
    # Dockless Trips by Operator
    df = pd.read_sql("""SELECT * FROM crosstab($$
                        SELECT DISTINCT
                        main.startutc::date AS date,
                        main.operatorclean,
                        COUNT(*) AS trips
                        FROM dockless_trips AS main
                        /*WHERE main.startutc::date >= '2017-09-20'*/
                        GROUP BY 1, 2
                        ORDER BY 1, 2$$
                        ,$$SELECT unnest('{jump,lime,mobike,ofo,spin}'::text[])$$)
                        AS ct ("date" date, "dless_trips_jump" int, "dless_trips_lime" int, "dless_trips_mobike" int, "dless_trips_ofo" int, "dless_trips_spin" int);
                                     """, con=conn)
    return df


def dockless_trip_distance_total(conn):
    # Calculate Cabi Bike Available based on bike min and max usage date, will ultimately be replaced by true CaBi Bike History
    df = pd.read_sql("""SELECT * FROM crosstab($$
                        SELECT DISTINCT
                        main.startutc::date AS date,
                        main.operatorclean,
                        SUM(ST_DistanceSpheroid(ST_SetSRID(st_makepoint(StartLongitude, StartLatitude),4326),
                        ST_SetSRID(st_makepoint(EndLongitude, EndLatitude),4326), 'SPHEROID["WGS 84",6378137,298.257223563]')) AS trip_dist
                        FROM dockless_trips AS main
                        /*WHERE main.startutc::date >= '2017-09-20'*/
                        GROUP BY 1, 2
                        ORDER BY 1, 2$$
                        ,$$SELECT unnest('{jump,lime,mobike,ofo,spin}'::text[])$$)
                    AS ct ("date" date, "dless_tripdist_tot_jump" numeric, "dless_tripdist_tot_lime" numeric, "dless_tripdist_tot_mobike" numeric, "dless_tripdist_tot_ofo" numeric, "dless_tripdist_tot_spin" numeric);
                     """, con=conn)
    return df


def dockless_trip_distance_avg(conn):
    # Calculate Cabi Bike Available based on bike min and max usage date, will ultimately be replaced by true CaBi Bike History
    df = pd.read_sql("""SELECT * FROM crosstab($$
                        SELECT DISTINCT
                        main.startutc::date AS date,
                        main.operatorclean,
                        AVG(ST_DistanceSpheroid(ST_SetSRID(st_makepoint(StartLongitude, StartLatitude),4326),
                        ST_SetSRID(st_makepoint(EndLongitude, EndLatitude),4326), 'SPHEROID["WGS 84",6378137,298.257223563]')) AS trip_dist
                        FROM dockless_trips AS main
                        /*WHERE main.startutc::date >= '2017-09-20'*/
                        GROUP BY 1, 2
                        ORDER BY 1, 2$$
                        ,$$SELECT unnest('{jump,lime,mobike,ofo,spin}'::text[])$$)
                    AS ct ("date" date, "dless_tripdist_avg_jump" numeric, "dless_tripdist_avg_lime" numeric, "dless_tripdist_avg_mobike" numeric, "dless_tripdist_avg_ofo" numeric, "dless_tripdist_avg_spin" numeric);
                     """, con=conn)
    return df


def dockless_overlap(conn):
    # Determine if Dockless trip start and ends with quarter mile of Cabi Station and if the Cabi station is empty at trip start time
    df = pd.read_sql("""SELECT DISTINCT
                        dless.startutc::date as date,
                        dless.operatorclean as operator,
                        SUM(CASE WHEN ST_DistanceSpheroid(ST_SetSRID(st_makepoint(StartLongitude, StartLatitude),4326),
                            ST_SetSRID(st_makepoint(start_station.lon, start_station.lat),4326),
                            'SPHEROID["WGS 84",6378137,298.257223563]') < 402.336 THEN 1 ELSE 0 END) / COUNT(*) :: float as dless_geo_start,
                        SUM(CASE WHEN ST_DistanceSpheroid(ST_SetSRID(st_makepoint(EndLongitude, EndLatitude),4326),
                            ST_SetSRID(st_makepoint(end_station.lon, end_station.lat),4326),
                            'SPHEROID["WGS 84",6378137,298.257223563]') < 402.336 THEN 1 ELSE 0 END) / COUNT(*) :: float as dless_geo_end,
                        SUM(CASE WHEN start_out_hist.status = 'empty' THEN 1 ELSE 0 END) / COUNT(*) :: float as dless_cap_start
                        FROM dockless_trips as dless
                        CROSS JOIN LATERAL
                        (SELECT short_name, lon, lat
                           FROM cabi_stations_temp
                           ORDER BY
                             ST_SetSRID(st_makepoint(dless.StartLongitude, dless.StartLatitude),4326) <-> ST_SetSRID(st_makepoint(lon, lat),4326)
                           LIMIT 1) as start_station
                        CROSS JOIN LATERAL
                        (SELECT short_name, lon, lat
                           FROM cabi_stations_temp
                           ORDER BY
                             ST_SetSRID(st_makepoint(dless.EndLongitude, dless.EndLatitude),4326) <-> ST_SetSRID(st_makepoint(lon, lat),4326)
                           LIMIT 1) as end_station
                        LEFT JOIN cabi_out_hist as start_out_hist
                        ON (start_station.short_name = start_out_hist.terminal_number) AND (dless.startutc BETWEEN start_out_hist.start_time AND start_out_hist.end_time)

                        /*WHERE dless.startutc::date >= '2017-09-20'*/
                        GROUP BY 1, 2;
                     """, con=conn)
    return df
