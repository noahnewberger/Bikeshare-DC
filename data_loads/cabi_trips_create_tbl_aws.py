import psycopg2
import getpass

host = "capstone-bikeshare.cs9te7lm3pt2.us-east-1.rds.amazonaws.com"
port = 5432
database = "bikeshare"
user = input("Enter your user name: ")
password = getpass.getpass("Enter your password: ")

conn = psycopg2.connect(host=host, user=user, port=port, password=password, database=database)
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
