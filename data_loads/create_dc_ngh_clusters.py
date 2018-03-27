import util_functions as uf

# This script creates the CaBi System information AWS table

if __name__ == "__main__":

    uf.set_env_path()
    conn, cur = uf.aws_connect()
    cur.execute("""
    DROP TABLE IF EXISTS dc_ngh_clusters;
    CREATE TABLE dc_ngh_clusters (
        name varchar(50),
        ngh_names varchar(200),
        objectid integer PRIMARY KEY,
        shape_area numeric,
        shape_length numeric,
        type varchar(50),
        web_url varchar(50),
        coordinates text
    )
    """)
    conn.commit()
