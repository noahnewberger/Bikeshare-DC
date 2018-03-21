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
CREATE TABLE cabi_out_hist(
    terminal_number integer,
    status varchar(20),
    start_time timestamp,
    end_time timestamp,
    duration integer
    )
""")
conn.commit()