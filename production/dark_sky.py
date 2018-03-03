import datetime
import pandas as pd
import forecastio
import time
import os


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


# Define Range of Date to pull forecast
start_date = datetime.datetime(2010, 1, 1)
end_date = datetime.datetime(2017, 12, 31)
delta = end_date - start_date

# List of APIs to loop through, 1000 calls per API
api_key_list = open('dark_sky_apis.txt').read().splitlines()

results = []
for api_key in api_key_list:
    # Ensure that max of 1000 calls per api key
    api_counter = 0
    for i in range(delta.days + 1):
        d = start_date + datetime.timedelta(days=i)
        # get daily weather attributes
        row_df = daily_weather(api_key, d)
        results.append(row_df)
        # API Counter to determine max call per API
        api_counter += 1
        # Substract one from delta so that range of dates isn't duplicated
        delta - datetime.timedelta(days=1)
        print("Count: {}, Date: {}". format(api_counter, d))
        # Break loop if reaching API call max, 975
        if (api_counter == 980) or (d == end_date):
            start_date = d + datetime.timedelta(days=1)
            break

# Concatentate one big dataframe
results_df = pd.concat(results, axis=0)

# Define Dateline hours
results_df['daylightHours'] = (results_df['sunsetTime'].astype(int) - results_df['sunriseTime'].astype(int)) / 3600

# Output final dataframe
TIMESTR = time.strftime("%Y%m%d_%H%M%S")
filename = "Dark_Sky_2010_2017" + TIMESTR + ".csv"
filepath = os.path.join("./Output", filename)
results_df.to_csv(filepath, index=True)

