from rest_framework import viewsets
from .models import Category,Product
from .serializers import SerializerCategory,SerializerProduct


class CategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = SerializerCategory

class ProductView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = SerializerProduct