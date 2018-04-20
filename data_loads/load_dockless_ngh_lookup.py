import util_functions as uf


def create_dockless_ngh_lookup(cur):
    # This script creates the dockless trips AWS table, note that Jump data is not accurate due to two decimal lat, lon
    cur.execute("""
    DROP TABLE IF EXISTS dockless_ngh_lookup;
    create table dockless_ngh_lookup as
    select distinct lat, lon, nbh_names
    from
    (select distinct StartLatitude as lat, StartLongitude as lon
    from dockless_trips
    union
    select distinct EndLatitude as lat, EndLongitude lon
    from dockless_trips) as lat_lon
    LEFT JOIN ngh as a
    ON ST_Intersects(ST_SetSRID(st_makepoint(lat_lon.lon, lat_lon.lat),4326), a.polygon)    """)


if __name__ == "__main__":
    # Connect to AWS
    uf.set_env_path()
    conn, cur = uf.aws_connect()
    # Create docklesS_trips_geo from dockless_trips
    create_dockless_ngh_lookup(cur)
    # Commit changes to database
    conn.commit()
