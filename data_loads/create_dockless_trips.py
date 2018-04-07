import util_functions as uf

# This script creates the dockless trips AWS table

if __name__ == "__main__":

    uf.set_env_path()
    conn, cur = uf.aws_connect()
    cur.execute("""
    DROP TABLE dockless_trips;
    CREATE TABLE dockless_trips(
        X integer,
        Operator varchar(50),
        TripID varchar(50) PRIMARY KEY,
        BikeID varchar(50),
        UserID varchar(50),
        StartDate timestamp,
        EndDate timestamp,
        StartLatitude numeric,
        StartLongitude numeric,
        EndLatitude numeric,
        EndLongitude numeric,
        TripDistance numeric,
        MetersMoved numeric,
        StartWard numeric,
        EndWard numeric,
        Distance numeric,
        posct timestamp,
        endposct timestamp,
        startutc timestamp,
        endutc timestamp,
        UniqueTripID varchar(50),
        OperatorClean varchar(50)
    )
    """)
    conn.commit()