from rest_framework import serializers # serializere converts python objects to JSON and vice versa
from rest_framework.renderers import JSONRenderer

from .models import Women


class WomenModel:
    def __init__(self, title, content):
        self.title = title
        self.content = content

# We have to have the same attributes in Serializer class as attributes in the model class
class WomenSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    content = serializers.CharField()


def encode():
    model = WomenModel("Анджелина Джоли", "Анджелина Джоли")
    model_serialized = WomenSerializer(model)
    print(model_serialized.data, "Тип результата:", type(model_serialized.data), sep="\n")
    json = JSONRenderer().render(model_serialized.data)
    print(json)