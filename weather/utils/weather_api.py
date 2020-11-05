from django.conf import settings
import requests, json
from urllib.parse import urlencode
#from weather.exceptions import MissingDate, MissingLocation
import datetime
from statistics import mean, median

# Our WeatherAPI class that will do all the
# work of capturing and converting the parameters
# into the needed data
class WeatherAPI:

    # Main method to the build the request
    def getWeatherData(self, location, fromDate, toDate, useRaw=False):
        try:
            res =  self.call(location, fromDate, toDate)
            # Check if there was a solution from the API
            if('error' in res['data'] ):
                msg = res['data']['error'][0]['msg']
                raise Exception(msg)
            if(useRaw == True):
                # This would be used for the charts
                return res['data']
            else:
                return self.process(res['data'])
        except Exception as e:
            raise Exception(e)

    # Do the call to the external API
    def call(self, location, fromDate, toDate):
        baseUrl = 'http://api.worldweatheronline.com/premium/v1/past-weather.ashx?'
        queryString = {
            'q': location,
            'date': fromDate,
            'enddate': toDate,
            'format' : 'json',
            'key' : settings.API_KEY
        }
        print(baseUrl + urlencode(queryString))
        req =  requests.get(baseUrl + urlencode(queryString))
        return req.json()

    # Process the incoming data
    def process(self, dataDict):
        weatherData = dataDict['weather']
        temperatureList = []
        humidityList = []

        for day in weatherData:
            temperatureList.append(int(day["maxtempC"]))
            #loop through the hours to the the humidity
            for hour in day['hourly']:
                humidityList.append(int(hour['humidity']))

        temperature = {
                'average': mean(temperatureList),
                'median' : median(temperatureList),
                'max': max(temperatureList),
                'min': min(temperatureList)
            }
        humidity = {
                'average': mean(humidityList),
                'median' : median(humidityList),
                'min': min(humidityList),
                'max': max(humidityList)
            }

        return {
            'temperature': temperature,
            'humidity' : humidity,
            #'location': dataDict['data']['request']['query'],

            }
