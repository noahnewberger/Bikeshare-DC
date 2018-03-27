import util_functions as uf

# This script creates the CaBi System information AWS table

if __name__ == "__main__":

    uf.set_env_path()
    conn, cur = uf.aws_connect()
    cur.execute("""
    CREATE TABLE bike_events(
        id  varchar(500) PRIMARY KEY,
        final_date  date,
        summary varchar(500)
        )
    """)
    conn.commit()
