import util_functions as uf

# This script creates the CaBi System information AWS table

if __name__ == "__main__":

    uf.set_env_path()
    conn, cur = uf.aws_connect()
    cur.execute("""
    CREATE TABLE cabi_system(
        region_id serial PRIMARY KEY,
        name varchar(100),
        code text
    )
    """)
    conn.commit()
