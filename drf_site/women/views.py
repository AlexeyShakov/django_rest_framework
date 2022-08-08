from django.forms import model_to_dict
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
        all_data = Women.objects.all().values()
        # Response converts a dictionary into JSON
        return Response({'posts': list(all_data)})

    def post(self, request):
        new_data = Women.objects.create(
            title=request.data["title"],
            content=request.data["content"],
            cat_id=request.data["cat_id"]
        )
        # model_to_dict converts django model object to a dictionary
        return Response({"post": model_to_dict(new_data)})

# class WomenApiView(generics.ListAPIView):
#     # Takes all data from the DB table
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer
