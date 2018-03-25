import util_functions as uf

# This script creates the CaBi System information AWS table

if __name__ == "__main__":

    uf.set_env_path()
    conn, cur = uf.aws_connect()
    cur.execute("""
    CREATE TABLE dc_pop (
        pop_date timestamp PRIMARY KEY,
        citypop numeric,
        grow_rate numeric,
        pct_bike numeric
    )
    """)
    conn.commit()
