
from rest_framework import generics
from .models import BaseProduct
from .serializers import ProductSerializer
from base import serializers

from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404


class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = BaseProduct.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        print(serializer.validated_data)
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = title
        serializer.save(content=content)
        # return super().perform_create(serializer)

class ProductDetailAPIVIEW(generics.RetrieveAPIView):
    queryset = BaseProduct.objects.all()
    serializer_class = ProductSerializer

# class ProductListAPIVIEW(generics.ListAPIView):
#     queryset = BaseProduct.objects.all()
#     serializer_class = ProductSerializer


# --------------------------------------------------------------------
# function base view get, list, create 
@api_view(['GET','POST'])
def product_alt_view(request, pk=None, *args, **kwargs):
    method = request.method

    if method == 'GET':
        if pk is not None:
            obj = get_object_or_404(BaseProduct, pk=pk)
            serializer = ProductSerializer(obj,many=False)
            return Response(serializer.data)
        # get request detail view 

        # list view 
        queryset = BaseProduct.objects.all()
        serializer = ProductSerializer(queryset,many = True).data
        return Response(serializer)
        

    if method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            title = serializer.validated_data.get('title')
            content = serializer.validated_data.get('content') or None
            if content is None:
                content = title
            serializer.save(content=content)
            return Response(serializer.data)
        return Response({"invalid data"}, status=400)

# ---------------------------------------------------------------------------

