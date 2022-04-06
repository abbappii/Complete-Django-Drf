
from cgitb import lookup
from rest_framework import authentication, generics, mixins, permissions
from .models import BaseProduct
from .serializers import ProductSerializer
from base import serializers

from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404


# ------------------------------------------------------------------------------
# generics view practice 

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



class ProductUpdateAPIVIEW(generics.UpdateAPIView):
    queryset = BaseProduct.objects.all()
    serializer_class = ProductSerializer

    # update view e look up view need 
    lookup_field = 'pk'

    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.title



class ProductDeleteAPIVIEW(generics.DestroyAPIView):
    queryset = BaseProduct.objects.all()
    serializer_class = ProductSerializer

    # update view e look up view need 
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        super().perform_destroy(instance)
    
# class ProductListAPIVIEW(generics.ListAPIView):
#     queryset = BaseProduct.objects.all()
#     serializer_class = ProductSerializer

# ---------------------------------------------------------------------

# generics mixin view 
class ProductMixinView(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    generics.GenericAPIView
    ):
    queryset = BaseProduct.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
    
    # get list and single product retrive 
    def get(self,request, *args, **kwargs):
        pk = kwargs.get('pk')
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request,*args, **kwargs)

    # create product 
    def post(self,request, *args, **kwargs):
        return self.create(request, *args,**kwargs)

    def perform_create(self, serializer):
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = 'it was none that is the reason to add content here.'
        serializer.save(content=content)

# ----------------------------------------------------------------------
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

