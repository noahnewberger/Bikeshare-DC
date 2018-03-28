import util_functions as uf

# This script creates the CaBi Station information with geopolitical borders to AWS table

if __name__ == "__main__":

    uf.set_env_path()
    conn, cur = uf.aws_connect()
    cur.execute("""
    DROP TABLE cabi_stations_geo_temp;
    CREATE TABLE cabi_stations_geo_temp(
        capacity integer,
        eightd_has_key_dispenser boolean,
        lat numeric,
        lon numeric,
        name varchar(200),
        region_id integer,
        rental_methods varchar(200),
        rental_url varchar(200),
        short_name varchar(20),
        station_id integer PRIMARY KEY,
        cluster_name varchar(20),
        ngh_names varchar(300),
        anc varchar(10),
        ward varchar(10)
    )
    """)
    conn.commit()
