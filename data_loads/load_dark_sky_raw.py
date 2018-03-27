import datetime
import pandas as pd
import forecastio
import time
import util_functions as uf
import os

# This script loads data to the dark_sky_raw AWS table


def daily_weather(api_key, d):
    # Pull historical daily weather from Dark Sky API
    lat = 38.9072
    lng = -77.0369
    # Pull Daily forcast from Dark Sky API
    forecast = forecastio.load_forecast(api_key, lat, lng, time=d)
    daily = forecast.daily()
    # Convert daily data dictionary to dataframe
    daily_data = daily.data[0].d
    daily_data_df = pd.DataFrame(daily_data, index=[d])
    return daily_data_df


if __name__ == "__main__":
    # Connect to AWS
    uf.set_env_path()
    conn, cur = uf.aws_connect()

    # Define Range of Date to pull forecast and turn into a list
    start_date = datetime.datetime(2018, 1, 1)
    end_date = datetime.datetime(2018, 3, 22)
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
    # Fill in zeros missing data
    results_df.fillna(0, inplace=True)
    # Convert precipIntensityMaxTime to integer
    results_df['precipIntensityMaxTime'] = results_df['precipIntensityMaxTime'].astype('int')
    # Drop weather fields new to 2018
    results_df = results_df.drop(['ozone', 'uvIndex', 'uvIndexTime', 'windGust', 'windGustTime'], axis=1)
    # Output final dataframe
    TIMESTR = time.strftime("%Y%m%d_%H%M%S")
    outname = "Dark_Sky_From_" + start_date.strftime('%Y-%m-%d') + "_To_" + end_date.strftime('%Y-%m-%d')
    results_df.to_csv(outname + ".csv", index=False, sep='|')
    # Load to Database
    uf.aws_load(outname, "dark_sky_raw", cur)
    # Commit changes to database
    conn.commit()
