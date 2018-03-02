import datetime
import pandas as pd
import requests
import os
import time


def daily_weather(api_key, d):
    ''' Pull historical daily weather from Dark Sky API'''

    # DC latitude and longitude coordinate
    lat = 38.9072
    lng = -77.0369

    # Define Request Path
    params = {'exclude': 'currently,flags'}
    unix_time = time.mktime(d.timetuple())
    loc_date = str(lat) + "," + str(lng) + "," + str(int(unix_time))
    dark_sky_url = "https://api.darksky.net/forecast"
    request_path = os.path.join(dark_sky_url, api_key, loc_date)

    # Make Request of API
    resp = requests.get(request_path, params=params)

    # Convert daily data dictionary to dataframe
    daily = resp.json()['daily']['data'][0]
    daily_df = pd.DataFrame(daily, index=[d])
    return daily_df


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
        if (api_counter == 975) or (d == end_date):
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

