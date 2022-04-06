from importlib import import_module
from rest_framework import viewsets
from .models import BaseProduct
from .serializers import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = BaseProduct.objects.all()
    serializer_class = ProductSerializer

    lookup_field = 'pk'