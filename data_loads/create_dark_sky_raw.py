import psycopg2
import os
from pathlib import Path
from dotenv import load_dotenv

env_path = Path('..') / '.env'
load_dotenv(dotenv_path=env_path)

host = "capstone-bikeshare.cs9te7lm3pt2.us-east-1.rds.amazonaws.com"
port = 5432
database = "bikeshare"
user = os.environ.get("AWS_USER")
password = os.environ.get("AWS_PASS")

conn = psycopg2.connect(host=host, user=user, port=port, password=password, database=database)
cur = conn.cursor()
cur.execute("""
CREATE TABLE dark_sky_raw(
    apparentTemperatureHigh numeric,
    apparentTemperatureHighTime integer,
    apparentTemperatureLow numeric,
    apparentTemperatureLowTime integer,
    apparentTemperatureMax numeric,
    apparentTemperatureMaxTime integer,
    apparentTemperatureMin numeric,
    apparentTemperatureMinTime integer,
    cloudCover numeric,
    dewPoint numeric,
    humidity numeric,
    icon varchar(500),
    moonPhase numeric,
    precipAccumulation numeric,
    precipIntensity numeric,
    precipIntensityMax numeric,
    precipIntensityMaxTime integer,
    precipProbability numeric,
    precipType varchar(20),
    pressure numeric,
    summary varchar(500),
    sunriseTime integer,
    sunsetTime integer,
    temperatureHigh numeric,
    temperatureHighTime integer,
    temperatureLow numeric,
    temperatureLowTime integer,
    temperatureMax numeric,
    temperatureMaxTime integer,
    temperatureMin numeric,
    temperatureMinTime integer,
    day_time integer,
    visibility numeric,
    weather_date date PRIMARY KEY UNIQUE NOT NULL,
    windBearing numeric,
    windSpeed numeric
    )
""")
conn.commit()

# Note can convert unicode to timestamp in postgres with this function SELECT to_timestamp(1195374767);
