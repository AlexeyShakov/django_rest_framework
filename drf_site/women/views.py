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
        all_posts = Women.objects.all()
        # Response converts QuerySet type to JSON
        return Response({'posts': WomenSerializer(all_posts, many=True).data})

    def post(self, request):
        # Handling the error when the input is insufficient or redundant
        serializer = WomenSerializer(data=request.data) # requets comes from the POST request
        # Checking that we get the appropriate amount of data
        serializer.is_valid(raise_exception=True)
        # Create new istance
        new_data = Women.objects.create(
            title=request.data["title"],
            content=request.data["content"],
            cat_id=request.data["cat_id"]
        )
        # model_to_dict converts django model object to a dictionary
        return Response({"post": WomenSerializer(new_data).data})

# class WomenApiView(generics.ListAPIView):
#     # Takes all data from the DB table
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer
