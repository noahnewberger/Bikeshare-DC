import util_functions as uf

# This script creates the CaBi Overage Pricing AWS table

if __name__ == "__main__":

    uf.set_env_path()
    conn, cur = uf.aws_connect()
    cur.execute("""
    CREATE TABLE jump_price(
        min_seconds integer PRIMARY KEY,
        max_seconds integer,
        cost numeric
        )
    """)
    conn.commit()
