from rest_framework.exceptions import APIException


class MissingDate(APIException):
    status_code = 400
    default_detail = "Missing Date."
    default_code = "missing_date"

class MissingLocation(APIException):
    status_code = 400
    default_detail = "Missing location."
    default_code = "missing_location"