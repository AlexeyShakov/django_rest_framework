from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from .models import Women
from .serializers import WomenSerializer
from rest_framework.views import APIView

# Create your views here.

class WomenApiView(APIView):
    # This method handles GET requests
    def get(self, request):
        # Response converts a dictionary into JSON
        return Response({'title': 'Анджолина Джоли'})

# class WomenApiView(generics.ListAPIView):
#     # Takes all data from the DB table
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer
