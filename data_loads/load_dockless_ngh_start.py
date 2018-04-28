import util_functions as uf


def create_dockless_ngh_start(cur):
    # This script creates the dockless trips AWS table, note that Jump data is not accurate due to two decimal lat, lon
    cur.execute("""
    DROP TABLE IF EXISTS dockless_ngh_start;
    create table dockless_ngh_start as
    select distinct
    tripid,
    operatorclean,
    StartLatitude,
    StartLongitude,
    nbh_names as start_nbh_names
    from
    (select tripid, operatorclean, StartLatitude, StartLongitude
    from dockless_trips) as trips
    LEFT JOIN ngh as a
    ON ST_Intersects(ST_SetSRID(st_makepoint(trips.StartLongitude, trips.StartLatitude),4326), a.polygon)""")


if __name__ == "__main__":
    # Connect to AWS
    uf.set_env_path()
    conn, cur = uf.aws_connect()
    # Create docklesS_trips_geo from dockless_trips
    create_dockless_ngh_start(cur)
    # Commit changes to database
    conn.commit()
