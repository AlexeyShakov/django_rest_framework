import io

from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from .models import Women

# # For demonstrating how to work encoding and decoding
# class WomenModel:
#     def __init__(self, title, content):
#         self.title = title
#         self.content = content
#
# def encode():
#     model = WomenModel("Angelina Jolie", "Content: Angelina Jolie")
#     model_serialized = WomenSerializer(model)
#     print(model_serialized.data, "Тип результата:", type(model_serialized.data), sep="\n")
#     json = JSONRenderer().render(model_serialized.data)
#     print(json)
#
#
# def decode():
#     stream = io.BytesIO(b'{"title":"Angelina Jolie","content":"Content: Angelina Jolie"}')
#     data = JSONParser().parse(stream)
#     # Desirializing data
#     serializer = WomenSerializer(data=data)
#     # Checking that the data is correct
#     serializer.is_valid()
#     print(serializer.validated_data, "Тип результата:", type(serializer.validated_data))

# Serializer converts python objects to JSON and vice versa. Moreover Serializser has to add, delete and update
# data in the DB
# We have to have the same attributes in Serializer class as attributes in the model class
class WomenSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    content = serializers.CharField()
    time_create = serializers.DateTimeField(read_only=True)
    time_update = serializers.DateTimeField(read_only=True)
    is_published = serializers.BooleanField(default=True)
    cat_id = serializers.IntegerField()


