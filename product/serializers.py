from rest_framework.serializers import ModelSerializer, ValidationError
from .models import Category,Product



class SerializerCategory(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'



class SerializerProduct(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
