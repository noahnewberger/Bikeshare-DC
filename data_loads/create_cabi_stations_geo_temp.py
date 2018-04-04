import util_functions as uf

# This script creates the CaBi Station information with geopolitical borders to AWS table

if __name__ == "__main__":

    uf.set_env_path()
    conn, cur = uf.aws_connect()
    cur.execute("""
    DROP TABLE cabi_stations_geo_temp;
    CREATE TABLE cabi_stations_geo_temp(
        start_short_name varchar(20),
        end_short_name varchar(20),
        start_capacity integer,
        start_eightd_has_key_dispenser boolean,
        start_lat numeric,
        start_lon numeric,
        start_name varchar(200),
        start_region_id integer,
        start_rental_methods varchar(200),
        start_rental_url varchar(200),
        start_station_id integer,
        start_region_code varchar(10),
        start_cluster_name varchar(20),
        start_ngh_names varchar(300),
        start_anc varchar(10),
        start_ward varchar(10),
        end_capacity integer,
        end_eightd_has_key_dispenser boolean,
        end_lat numeric,
        end_lon numeric,
        end_name varchar(200),
        end_region_id integer,
        end_rental_methods varchar(200),
        end_rental_url varchar(200),
        end_station_id integer,
        end_region_code varchar(10),
        end_cluster_name varchar(20),
        end_ngh_names varchar(300),
        end_anc varchar(10),
        end_ward varchar(10),
        dist_miles numeric
    )
    """)
    conn.commit()
