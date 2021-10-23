from rest_framework.exceptions import APIException
from rest_framework import status


class ValidationException(APIException):
    status_code = status.HTTP_422_UNPROCESSABLE_ENTITY
    default_detail = 'Invalid input.'
    default_code = 'invalid'

    def __init__(self, **kwargs):
        self.detail = kwargs['errors']


