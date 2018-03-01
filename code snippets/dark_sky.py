import forecastio
import datetime

api_key = "5c5f92f84b86bf7d7dc3668ebfec54f8"  # see Asana ticket for key
lat = 38.894432
lng = -77.013655


result = forecastio.load_forecast(api_key, lat, lng)


start_date = datetime.datetime(2015, 1, 15)
end_date = datetime.datetime(2018, 2, 17)
d = start_date
delta = datetime.timedelta(days=1)

forecast = forecastio.load_forecast(api_key, lat, lng, time=start_date)
daily = forecast.daily()

for daily_data in daily.data:
    precipIntensity = daily_data.precipIntensity
    precipIntensityMax = daily_data.precipIntensityMax
    #precipType = daily_data.precipType
    temperatureHigh = daily_data.temperatureHigh
    temperatureLow = daily_data.temperatureLow
    humidity = daily_data.humidity
    windSpeed = daily_data.windSpeed
    daylight_diff = (daily_data.sunsetTime - daily_data.sunriseTime)
    daylight_hours = daylight_diff.days * 24 + daylight_diff.seconds / 3600
    print(precipIntensity, precipIntensityMax, temperatureHigh, temperatureLow)
    print(humidity, windSpeed, daylight_hours)
