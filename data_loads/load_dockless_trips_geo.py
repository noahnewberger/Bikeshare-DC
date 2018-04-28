import util_functions as uf


def create_dockless_trips_geo(cur):
    # This script creates the dockless trips AWS table, note that Jump data is not accurate due to two decimal lat, lon
    cur.execute("""
    DROP TABLE IF EXISTS dockless_trips_geo;
    CREATE TABLE dockless_trips_geo as
    SELECT
    dless.tripid,
    dless.uniquetripid,
    dless.operatorclean,
    dless.bikeid,
    dless.startutc,
    dless.endutc,
    anc_start.start_anc,
    anc_end.end_anc,
    ngh_start.start_nbh_names,
    ngh_end.end_nbh_names,
    dless.startlatitude,
    dless.StartLongitude,
    dless.endlatitude,
    dless.endLongitude,
    /* Calculate Trip Distance in Meters*/
    ST_DistanceSpheroid(ST_SetSRID(st_makepoint(StartLongitude, StartLatitude),4326),
    ST_SetSRID(st_makepoint(endLongitude, endlatitude),4326),
    'SPHEROID["WGS 84",6378137,298.257223563]') as TripDistance_Meters_Calc,
    /* Calculate Distance to Closest CaBi Station from Start Point*/
    ST_DistanceSpheroid(ST_SetSRID(st_makepoint(StartLongitude, StartLatitude),4326),
    ST_SetSRID(st_makepoint(start_station.lon, start_station.lat),4326),
    'SPHEROID["WGS 84",6378137,298.257223563]') as StCaBi_Distance_Meters,
    start_station.short_name as st_station,
    start_out_hist.status as st_station_status,
    /* Determine if closest CaBi Station is a quarter mile or less away to start point*/
    CASE WHEN ST_DistanceSpheroid(ST_SetSRID(st_makepoint(StartLongitude, StartLatitude),4326),
    ST_SetSRID(st_makepoint(start_station.lon, start_station.lat),4326),
    'SPHEROID["WGS 84",6378137,298.257223563]') < 402.336 THEN 1 ELSE 0 END as st_geo_overlap,
    /* Determine if Closest Start Station Cabi Station was empty at start of dockless trip */
    CASE WHEN start_out_hist.status = 'empty' THEN 1 ELSE 0 END as st_cap_overlap,
    /* Calculate Distance to Closest CaBi Station from End Point*/
    ST_DistanceSpheroid(ST_SetSRID(st_makepoint(EndLongitude, EndLatitude),4326),
    ST_SetSRID(st_makepoint(end_station.lon, end_station.lat),4326),
    'SPHEROID["WGS 84",6378137,298.257223563]') as EndCaBi_Distance_Meters,
    end_station.short_name as end_station,
    /* Determine if closest CaBi Station is a quarter mile or less away to end point*/
    CASE WHEN ST_DistanceSpheroid(ST_SetSRID(st_makepoint(EndLongitude, EndLatitude),4326),
    ST_SetSRID(st_makepoint(end_station.lon, end_station.lat),4326),
    'SPHEROID["WGS 84",6378137,298.257223563]') < 402.336 THEN 1 ELSE 0 END as end_geo_overlap
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
    LEFT JOIN (select * FROM cabi_out_hist WHERE start_time::date >='2017-9-01' and status = 'empty') as start_out_hist
    ON dless.startutc BETWEEN start_out_hist.start_time AND start_out_hist.end_time
    /* JOIN ON ANC START*/
    LEFT JOIN dockless_anc_start as anc_start
    ON dless.tripid = anc_start.tripid and dless.operatorclean = anc_start.operatorclean
    /* JOIN ON ANC END*/
    LEFT JOIN dockless_anc_end as anc_end
    ON dless.tripid = anc_end.tripid and dless.operatorclean = anc_end.operatorclean

    """)


if __name__ == "__main__":
    # Connect to AWS
    uf.set_env_path()
    conn, cur = uf.aws_connect()
    # Create docklesS_trips_geo from dockless_trips
    print("Create Dockless Trips Geo")
    create_dockless_trips_geo(cur)
    # Commit changes to database
    conn.commit()
