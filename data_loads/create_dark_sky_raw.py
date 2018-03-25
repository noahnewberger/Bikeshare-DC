import util_functions as uf

# This script creates the dark sky raw AWS Table

if __name__ == "__main__":

    uf.set_env_path()
    conn, cur = uf.aws_connect()

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
