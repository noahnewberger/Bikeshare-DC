import util_functions as uf

# This script creates the CaBi System information AWS table

if __name__ == "__main__":

    uf.set_env_path()
    conn, cur = uf.aws_connect()
    cur.execute("""
    CREATE TABLE cabi_stations_temp(
        capacity integer,
        eightd_has_key_dispenser boolean,
        eightd_station_services varchar(500),
        lat numeric,
        lon numeric,
        name varchar(200),
        region_id integer,
        rental_methods varchar(200),
        rental_url varchar(200),
        short_name varchar(20),
        station_id integer PRIMARY KEY
    )
    """)
    conn.commit()
