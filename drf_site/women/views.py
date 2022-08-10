from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from .models import Women, Category
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from .serializers import WomenSerializer
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated


# Create your views here.

# class WomenViewSet(viewsets.ModelViewSet):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer
#
#     # This method allows us to get only certain data from the DB
#     def get_queryset(self):
#         # If we don't do that then when we wanna get the certain post we will get the error. So
#         pk = self.kwargs.get("pk")
#         if not pk:
#             return Women.objects.all()[:3]
#         return Women.objects.filter(pk=pk)
#
#     # This decorator is needed to create new endpoints for our Router class. It will have the URL:
#     # "api/v1/women/category/"
#     @action(methods=["get"], detail=True)
#     def category(self, request, pk=None):
#         cats = Category.objects.get(pk=pk)
#         return Response({"cats": cats.name})

# Old version with repeating code

# own pagination class for certain endpoint
class WomenApiListPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = "page_size"
    max_page_size = 1000


# This class handles GET and POST requests
class WomenApiList(generics.ListCreateAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    # It's needed to limit the rights of a user
    permission_classes = (IsAuthenticatedOrReadOnly, )
    pagination_class = WomenApiListPagination


# Implementing PUT and PATCH requests
class WomenApiUpdate(generics.RetrieveUpdateAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    permission_classes = (IsAuthenticated, )
    # We clarify which authentification we wanna use
    # authentication_classes = (TokenAuthentication,)


class WomenRUD(generics.RetrieveDestroyAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    permission_classes = (IsAdminOrReadOnly, )





