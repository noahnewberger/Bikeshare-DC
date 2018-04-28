import util_functions as uf


def create_dockless_anc_end(cur):
    # This script creates the dockless trips AWS table, note that Jump data is not accurate due to two decimal lat, lon
    cur.execute("""
    DROP TABLE IF EXISTS dockless_anc_end;
    create table dockless_anc_end as
    select distinct
    tripid,
    operatorclean,
    EndLatitude,
    EndLongitude,
    anc_id as end_anc
    from
    (select tripid, operatorclean, EndLatitude, EndLongitude
    from dockless_trips) as trips
    LEFT JOIN anc as a
    ON ST_Intersects(ST_SetSRID(st_makepoint(trips.EndLongitude, trips.EndLatitude),4326), a.polygon)""")


if __name__ == "__main__":
    # Connect to AWS
    uf.set_env_path()
    conn, cur = uf.aws_connect()
    # Create docklesS_trips_geo from dockless_trips
    create_dockless_anc_end(cur)
    # Commit changes to database
    conn.commit()
