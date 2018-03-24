import util_functions as uf

# This script creates the CaBi outage history AWS Table

if __name__ == "__main__":

    uf.set_env_path()
    conn, cur = uf.aws_connect()
    cur.execute("""
    CREATE TABLE cabi_trips(
        duration integer,
        start_date timestamp,
        end_date timestamp,
        start_station varchar(20),
        end_station varchar(20),
        bike_number varchar(30),
        member_type varchar(20)
    )
    """)
    conn.commit()
