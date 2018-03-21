import datetime
import pandas as pd
import forecastio
import time
import os
import math
from pathlib import Path
from dotenv import load_dotenv
import psycopg2


# Initialize .env file
env_path = Path('..') / '.env'
load_dotenv(dotenv_path=env_path)


host = "capstone-bikeshare.cs9te7lm3pt2.us-east-1.rds.amazonaws.com"
port = 5432
database = "bikeshare"
user = os.environ.get("AWS_USER")
password = os.environ.get("AWS_PASS")


# Connect to aws postgres DB
conn = psycopg2.connect(host=host, user=user, port=port, password=password, database=database)
cur = conn.cursor()


def daily_weather(api_key, d):
    ''' Pull historical daily weather from Dark Sky API'''

    # DC latitude and longitude coordinate
    lat = 38.9072
    lng = -77.0369

    # Pull Daily forcast from Dark Sky API
    forecast = forecastio.load_forecast(api_key, lat, lng, time=d)
    daily = forecast.daily()

    # Convert daily data dictionary to dataframe
    daily_data = daily.data[0].d
    daily_data_df = pd.DataFrame(daily_data, index=[d])
    return daily_data_df


# Define Range of Date to pull forecast and turn into a list
start_date = datetime.datetime(2010, 10, 1)
end_date = datetime.datetime(2017, 12, 31)

delta = end_date - start_date
date_list = [start_date + datetime.timedelta(days=i) for i in range(delta.days + 1)]

# Define API Key List
api_key = os.environ.get('DARK_SKY_API')

# Loop through dates and pull weather data
results = []
for d in date_list:
    # get daily weather attributes
    row_df = daily_weather(api_key, d)
    row_df['weather_date'] = d
    results.append(row_df)
    print('{} has been processed'.format(d))

# Concatentate one big dataframe
results_df = pd.concat(results, axis=0)

# Fill in zeros for precipication fields
values = {'precipIntensityMaxTime': 0,
          'precipAccumulation': 0,
          'precipIntensity': 0,
          'precipIntensityMax': 0,
          'precipProbability': 0,
          'cloudCover': 0}
results_df.fillna(value=values, inplace=True)
results_df['precipIntensityMaxTime'] = results_df['precipIntensityMaxTime'].astype('int')
print(results_df['cloudCover'].tail())
# Output final dataframe
TIMESTR = time.strftime("%Y%m%d_%H%M%S")
outname = "Dark_Sky_From_" + start_date.strftime('%Y-%m-%d') + "_To_" + end_date.strftime('%Y-%m-%d')
results_df.to_csv(outname + ".csv", index=False, sep='|')


# Load to Database
with open(outname + ".csv", 'r') as f:
    # Skip the header row.
    next(f)
    cur.copy_from(f, 'dark_sky_raw', sep='|')
print("{} has been loaded to the dark_sky_raw database".format(outname))

# Commit changes to database
conn.commit()
