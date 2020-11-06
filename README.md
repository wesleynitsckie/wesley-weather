# Wesley' Weather Service

A Django based application which finds historic weather data for a given city

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
pip install -r requirements.txt
```

## Usage

```python
python manage.py runserver
```
Once the server is running open your browser and go to:
[http://127.0.0.1:8000](http://127.0.0.1:8000/)

## API Example

**Base Url**: ```http://127.0.0.1:8000/api```
 > Parameters:
 - **location**: *String*  [A name of a city] *Required*
 - **fromDate**: *Date* [format: YYYY-MM-DD] *Required*
 - **toDate**: *Date* [format: YYYY-MM-DD] *Required*

> Example
```python
http://127.0.0.1:8000/api?location=Pretoria&fromDate=2020-07-01&toDate=2020-07-30
```
> Sample Response
```json
{
    "temperature": {
        "average": 20.533333333333335,
        "median": 20.5,
        "max": 26,
        "min": 13
    },
    "humidity": {
        "average": 32.983333333333334,
        "median": 29.0,
        "min": 6,
        "max": 86
    }
}
```
## API Example
```python
python manage.py test
```

## License
[MIT](https://choosealicense.com/licenses/mit/)