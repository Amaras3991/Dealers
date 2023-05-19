from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import APIException, AuthenticationFailed
from rest_framework.authentication import get_authorization_header
from .models import Car, SellInfo

class CarsViewApi(APIView):
    def get(self, request):
        car = []
