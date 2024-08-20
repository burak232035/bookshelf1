from django.shortcuts import render

# Create your views here.

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view

class ApiTestView(APIView):
    @api_view(['GET'])
    def api_test(self, request):
        return Response("get api")