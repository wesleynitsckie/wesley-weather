from django.test import TestCase

# Create your tests here.
class WeatherTest(TestCase):
    
    def test_was_requested_succcessfully(self):
        self.assertIs(1, 1)