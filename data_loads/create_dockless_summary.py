import util_functions as uf

# This script creates the dockless summary AWS table

if __name__ == "__main__":

    uf.set_env_path()
    conn, cur = uf.aws_connect()
    cur.execute("""
    CREATE TABLE dockless_summary(
        Operator integer,
        Month integer,
        TotalTrips integer,
        TotalBikes integer,
        TotalCrashes integer,
        TotalInjuries integer,
        Parking integer,
        NonOperationalLS integer,
        Lights integer,
        WheelTire integer,
        Seat integer,
        Brakes integer,
        Frame integer,
        GearSystem integer,
        Lock integer,
        OtherRepair integer,
        NonOperationalM integer
    )
    """)
    conn.commit()
