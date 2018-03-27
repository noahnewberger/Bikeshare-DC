import util_functions as uf

# This script creates the CaBi outage history AWS Table

if __name__ == "__main__":

    uf.set_env_path()
    conn, cur = uf.aws_connect()
    cur.execute("""
    CREATE TABLE cabi_out_hist(
        terminal_number integer,
        status varchar(20),
        start_time timestamp,
        end_time timestamp,
        duration integer
        )
    """)
    conn.commit()
