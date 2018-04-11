import pandas as pd


def dark_sky(conn):
    # All weather data from Dark Sky
    df = pd.read_sql("""SELECT  weather_date as date,
                        EXTRACT('year' FROM weather_date) as year,
                        EXTRACT('quarter' FROM weather_date) as quarter,
                        EXTRACT('month' FROM weather_date) as month,
                        EXTRACT('dow' FROM weather_date) as day_of_week,
                        EXTRACT('hour' FROM to_timestamp(apparenttemperaturehightime) at time zone 'america/new_york') as apparenttemperaturehightime,
                        EXTRACT('hour' FROM to_timestamp(apparenttemperaturelowtime) at time zone 'america/new_york') as apparenttemperaturelowtime,
                        EXTRACT('hour' FROM to_timestamp(temperaturehightime) at time zone 'america/new_york') as temperaturehightime,
                        EXTRACT('hour' FROM to_timestamp(temperaturelowtime) at time zone 'america/new_york') as temperaturelowtime,
                        EXTRACT('hour' FROM to_timestamp(precipintensitymaxtime) at time zone 'america/new_york') as precipintensitymaxtime,
                        EXTRACT('hour' FROM to_timestamp(sunrisetime) at time zone 'america/new_york') as sunrisetime,
                        EXTRACT('hour' FROM to_timestamp(sunsettime) at time zone 'america/new_york') as sunsettime,
                        EXTRACT('hour' FROM to_timestamp(day_time) at time zone 'america/new_york') as day_time,
                        EXTRACT('hour' FROM to_timestamp(sunsettime) at time zone 'america/new_york') - EXTRACT('hour' FROM to_timestamp(sunrisetime) at time zone 'america/new_york') as daylight_hours,
                        apparenttemperaturehigh,
                        apparenttemperaturelow,
                        temperaturehigh,
                        temperaturelow,
                        cloudcover,
                        dewpoint,
                        humidity,
                        moonphase,
                        precipaccumulation,
                        precipintensity,
                        precipintensitymax,
                        precipprobability,
                        pressure,
                        CASE WHEN preciptype = 'rain' THEN 1 ELSE 0 END as rain,
                        CASE WHEN preciptype = 'snow' THEN 1 ELSE 0 END as snow,
                        CASE WHEN preciptype = 'sleet' THEN 1 ELSE 0 END as sleet,
                        visibility,
                        windbearing,
                        windspeed
                        FROM dark_sky_raw
                        /*WHERE weather_date >= '2017-09-20'*/;
                        """, con=conn)
    return df
