import util_functions as uf

# This script creates the CaBi Overage Pricing AWS table

if __name__ == "__main__":

    uf.set_env_path()
    conn, cur = uf.aws_connect()
    cur.execute("""
    CREATE TABLE dockless_price(
        min_seconds integer PRIMARY KEY,
        max_seconds integer,
        limebike numeric,
        spin numeric,
        ofo numeric,
        mobike numeric
        )
    """)
    conn.commit()
