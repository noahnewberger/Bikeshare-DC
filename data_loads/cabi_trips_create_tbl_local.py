import psycopg2
conn = psycopg2.connect("host=localhost dbname=postgres user=postgres")
cur = conn.cursor()
cur.execute("""
CREATE TABLE cabi_trips(
    duration integer,
    start_date timestamp,
    end_date timestamp,
    start_station varchar(20),
    end_station varchar(20),
    bike_number varchar(30),
    member_type varchar(20)
)
""")
conn.commit()
