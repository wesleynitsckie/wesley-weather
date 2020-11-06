from django.test import TestCase

# Create your tests here.
class WeatherTest(TestCase):
    
    def test_index_loads_properly(self):
        """The index page loads properly"""
        response = self.client.get('http://localhost:8000')
        self.assertEqual(response.status_code, 200)

    def test_was_requested_succcessfully(self):
        response = self.client.get('http://localhost:8000/api?location=Pretoria&fromDate=2020-01-01&toDate=2020-01-30')
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIs(data['temperature']['max'], 35)

    def test_incorrect_date_format(self):
        response = self.client.get('http://localhost:8000/api?location=Pretoria&fromDate=2020-01-01&toDate=2020-01-300000')
        self.assertEqual(response.status_code, 428)

    def test_fail_weather_check(self):
        response = self.client.get('http://localhost:8000/api?location=asdfasdf&fromDate=2020-01-01&toDate=2020-01-30')
        self.assertEqual(response.status_code, 500)