import util_functions as uf

# This script creates the dockless trips AWS table

if __name__ == "__main__":

    uf.set_env_path()
    conn, cur = uf.aws_connect()
    cur.execute("""
    CREATE TABLE dockless_trips(
        Operator integer,
        TripID integer PRIMARY KEY,
        BikeID varchar(10),
        UserID varchar(20),
        StartTime timestamp,
        EndTime timestamp,
        StartLatitude numeric,
        StartLongitude numeric,
        EndLatitude numeric,
        EndLongitude numeric,
        TripDistance numeric
    )
    """)
    conn.commit()
