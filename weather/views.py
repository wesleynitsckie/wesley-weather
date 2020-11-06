from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render
from .utils.weather_api import WeatherAPI
from .utils.validator import Validator
from rest_framework.renderers import JSONRenderer
from rest_framework.views import exception_handler
from rest_framework import status

# Lets serve up the Front page 
def index(request):
    try:
        context = {}
        if( request.method == 'POST'):
            valid = Validator()
            if(valid.isValid(request.POST) == False):
                context = {
                        'error': 'Sorry, missing parameters',
                }
            location = request.POST['location']
            toDate = request.POST['toDate']
            fromDate = request.POST['fromDate']
            if((valid.isValidDate(toDate) == False) or (valid.isValidDate(fromDate) == False) ):
                context = {
                        'error': 'Invalid date or incorrect format. Accepted date format YYYY-MM-DD',
                    }
            weatherAPI =  WeatherAPI()
            result = weatherAPI.getWeatherData(location = location, fromDate = fromDate, toDate = toDate, useRaw=False)
            context = {
                'data': result,
                'fromDate': fromDate,
                'toDate': toDate,
                'location': location
            }
        return render(request, 'weather.html', context)
    except Exception as e:
        print(e)
        context = {
                    'error': str(e),
                }
        return render(request, 'weather.html', context)

# Our main API entry point
def getWeather(request):
    try:
        #Let do some validation
        valid = Validator()
        if(valid.isValid(request.GET) == False):
            return JsonResponse({"msg": "Sorry, missing parameters"}, safe=False, status=status.HTTP_428_PRECONDITION_REQUIRED)

        location = request.GET['location']
        toDate = request.GET['toDate']
        fromDate = request.GET['fromDate']
        if((valid.isValidDate(toDate) == False) or (valid.isValidDate(fromDate) == False) ):
            return JsonResponse({"msg": "Invalid date or incorrect format. Accepted date format YYYY-MM-DD"}, safe=False, status=status.HTTP_428_PRECONDITION_REQUIRED)

        weatherAPI =  WeatherAPI()
        result = weatherAPI.getWeatherData(location = location, fromDate = fromDate, toDate = toDate, useRaw=False)
        return JsonResponse(result, safe=False) 
    except Exception as e:
        print(e)
        return JsonResponse({"msg": str(e)}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# Handle thoughs 404's
def handler404(request):
    return render(request, '404.html', status=404)

# Handle thoughs 505's
def handler500(request):
    return render(request, '500.html', status=500)