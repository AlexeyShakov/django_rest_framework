from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.response import Response
from .models import Women
from .serializers import WomenSerializer
from rest_framework.views import APIView

# Create your views here.

class WomenViewSet(viewsets.ModelViewSet):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer


# # Old version with repeating code

# # This class handles GET and POST requests
# class WomenApiList(generics.ListCreateAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer
#
#
# # Implementing PUT and PATCH requests
# class WomenApiUpdate(generics.UpdateAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer
#
#
# class WomenRUD(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer





