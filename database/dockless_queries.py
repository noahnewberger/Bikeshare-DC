import pandas as pd


def dockless_trips_by_operator(conn):
    # Dockless Trips by Operator
    df = pd.read_sql("""SELECT * FROM crosstab($$
                        SELECT DISTINCT
                        main.startutc::date AS date,
                        main.operatorclean,
                        COUNT(*) AS trips
                        FROM dockless_trips AS main
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
                        GROUP BY 1, 2
                        ORDER BY 1, 2$$
                        ,$$SELECT unnest('{jump,lime,mobike,ofo,spin}'::text[])$$)
                    AS ct ("date" date, "dless_tripdist_avg_jump" numeric, "dless_tripdist_avg_lime" numeric, "dless_tripdist_avg_mobike" numeric, "dless_tripdist_avg_ofo" numeric, "dless_tripdist_avg_spin" numeric);
                     """, con=conn)
    return df


def dockless_overlap(conn):
    # Aggregate if Dockless trip start and ends with quarter mile of Cabi Station and if the Cabi station is empty at trip start time
    df = pd.read_sql("""SELECT DISTINCT
                        startutc::date as date,
                        operatorclean as operator,
                        SUM(st_geo_overlap) / COUNT(*) :: float as dless_geo_start,
                        SUM(end_geo_overlap) / COUNT(*) :: float as dless_geo_end,
                        SUM(st_cap_overlap) / COUNT(*) :: float as dless_cap_start
                        FROM dockless_trips_geo
                        GROUP BY 1, 2
                        ORDER BY 1, 2
                     """, con=conn)
    return df
