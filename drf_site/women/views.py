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

    # POST is for creating a new instance
    def post(self, request):
        # Handling the error when the input is insufficient or redundant
        serializer = WomenSerializer(data=request.data) # requets comes from the POST request
        # Checking that we get the appropriate amount of data
        serializer.is_valid(raise_exception=True)
        # The method below will call for create() method from Serializer class aytomatically
        serializer.save()
        # model_to_dict converts django model object to a dictionary
        return Response({"post": serializer.data})

    # PUT is for updating an existed instance
    def put(self, request, *args, **kwargs):
        # pk = primary key. PK allows us to understand which row will be updated
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Метод PUT не определен"})
        # Try to get the row needed
        try:
            instance = Women.objects.get(pk=pk)
        except:
            return Response({"error": "Метод PUT не определен"})
        # If everything alright then we work with date for updating(request_data) and the data we wanna change(instance)
        serializer = WomenSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"post": serializer.data})

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Метод DELETE не определен"})
        Women.objects.filter(pk=pk).delete()
        return Response({"post": "The post №" + " " + str(pk) + " has been deleted successfully"})



# class WomenApiView(generics.ListAPIView):
#     # Takes all data from the DB table
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer
