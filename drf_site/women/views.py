from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Women, Category
from .serializers import WomenSerializer
from rest_framework.views import APIView

# Create your views here.

class WomenViewSet(viewsets.ModelViewSet):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer

    # This method allows us to get only certain data from the DB
    def get_queryset(self):
        # If we don't do that then when we wanna get the certain post we will get the error. So
        pk = self.kwargs.get("pk")
        if not pk:
            return Women.objects.all()[:3]
        return Women.objects.filter(pk=pk)

    # This decorator is needed to create new endpoints for our Router class. It will have the URL:
    # "api/v1/women/category/"
    @action(methods=["get"], detail=True)
    def category(self, request, pk=None):
        cats = Category.objects.get(pk=pk)
        return Response({"cats": cats.name})

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





