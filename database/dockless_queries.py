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


def dockless_duration_cost(conn):
    # Average trip duration and cost where trips are great than a minute and less than a day.  Mobike not included
    df = pd.read_sql("""SELECT DISTINCT
                        startutc::date as date,
                        operatorclean as operator,
                        /* Convert Duration to Seconds*/
                        AVG(EXTRACT('hours' FROM (endutc - startutc)) * 3600 +
                        EXTRACT('minutes' FROM (endutc - startutc)) * 60 +
                        EXTRACT('seconds' FROM (endutc - startutc))) as avg_duration,
                        /* Assign appropriate price based on operator*/
                        AVG(COALESCE(
                        CASE WHEN operatorclean = 'lime' THEN price.limebike ELSE NULL END,
                        CASE WHEN operatorclean = 'ofo' THEN price.ofo ELSE NULL END,
                        CASE WHEN operatorclean = 'spin' THEN price.spin ELSE NULL END,
                        CASE WHEN operatorclean = 'jump' THEN jump_price.cost ELSE NULL END)) as avg_cost
                        FROM dockless_trips as trip_dur
                        /*Join on non-jump operator pricing*/
                        LEFT JOIN dockless_price as price
                        ON trip_dur.operatorclean != 'jump' AND EXTRACT('hours' FROM (endutc - startutc)) * 3600 +
                        EXTRACT('minutes' FROM (endutc - startutc)) * 60 +
                        EXTRACT('seconds' FROM (endutc - startutc)) BETWEEN price.min_seconds and price.max_seconds
                        /*Join on jump operator pricing*/
                        LEFT JOIN jump_price as jump_price
                        ON trip_dur.operatorclean = 'jump' AND EXTRACT('hours' FROM (endutc - startutc)) * 3600 +
                        EXTRACT('minutes' FROM (endutc - startutc)) * 60 +
                        EXTRACT('seconds' FROM (endutc - startutc)) BETWEEN jump_price.min_seconds and jump_price.max_seconds
                        WHERE endutc > startutc
                        AND '1 minute' < endutc - startutc
                        AND endutc - startutc < '1 day'
                        AND operatorclean != 'mobike'
                        GROUP BY 1, 2
                     """, con=conn)
    return df
