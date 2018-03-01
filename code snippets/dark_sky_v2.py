import forecastio
import datetime
import pandas as pd


def dark_sky_try(attribute):
    ''' tries to pull weather attribute from dark sky api, otherwise 0'''
    try:
        data_point = attribute
    except:
        data_point = 0
    return data_point


def data_points():
    '''Define dataframe of data for each API call'''
    daily = forecast.daily()
    for daily_data in daily.data:
        daylightDiff = (daily_data.sunsetTime - daily_data.sunriseTime)
        daylightHours = daylightDiff.days * 24 + daylightDiff.seconds / 3600
        data = {'precipProbability': dark_sky_try(daily_data.precipProbability),
                'precipIntensity': dark_sky_try(daily_data.precipIntensity),
                'precipIntensityMax': dark_sky_try(daily_data.precipIntensityMax),
                # 'precipType': dark_sky_try(daily_data.precipType),
                'temperatureHigh': dark_sky_try(daily_data.temperatureHigh),
                'temperatureLow': dark_sky_try(daily_data.temperatureLow),
                'humidity': dark_sky_try(daily_data.humidity),
                'windSpeed': dark_sky_try(daily_data.windSpeed),
                #'cloudCover': dark_sky_try(daily_data.cloudCover),
                'daylightHours': daylightHours}
        row_df = pd.DataFrame(data, index=[d])
        return row_df

# DC latitude and longitude coordinate
lat = 38.9072
lng = -77.0369

# Define Range of Date to pull forecast
start_date = datetime.datetime(2018, 1, 1)
end_date = datetime.datetime(2018, 1, 31)
delta = end_date - start_date

# List of APIs to loop through, 1000 calls per API
test_api = "5c5f92f84b86bf7d7dc3668ebfec54f8"
'''api_key_list = ['c36641115917f0eb030b3d286b05d89a',
                'e4f0147fc6fac69398e9fbd1ce79b720']'''
api_key_list = [test_api,
                test_api]


results = []
for api_key in api_key_list:
    # Ensure that max of 1000 calls per api key
    api_counter = 0
    for i in range(delta.days + 1):
        d = start_date + datetime.timedelta(days=i)
        forecast = forecastio.load_forecast(api_key, lat, lng, time=d)
        daily = forecast.daily()
        for daily_data in daily.data:
            import sys
            sys.exit()
        '''row_df = data_points()
        results.append(row_df)
        # API Counter to determine max call per API
        api_counter += 1
        # Substract one from delta so that range of dates isn't duplicated
        delta - datetime.timedelta(days=1)
        print("Count: {}, Date: {}". format(api_counter, d))
        # Break loop if reaching API call max, 975
        if (api_counter == 15) or (d == end_date):
            start_date = d + datetime.timedelta(days=1)
            break'''

# Concatentate one big dataframe
results_df = pd.concat(results, axis=0)
results_df.to_csv(r'./Output/weather_data.csv')
