# wesley-weather

## Local requirements
- Python 3.6 
- Install packages via pip:
```
pip install -r requirements.txt
```

Rename .env.sample to .env
Get an API key at https://www.worldweatheronline.com/

## Start the server
```
 python manage.py runserver
```

In your browser go to play around
```
http://127.0.0.1:8000/weather/
```

## API 
Base Url: http://127.0.0.1:8000/weather/api
parameters:
location:String  [A name of a city]
fromDate: Date [format: YYYY-MM-DD]
toDate: Date [format: YYYY-MM-DD]

Example:
http://127.0.0.1:8000/weather/api?location=Pretoria&fromDate=2020-01-01&toDate=2020-01-30