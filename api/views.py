from rest_framework.decorators import api_view
from rest_framework.response import Response
from base.models import BaseProduct
from base.serializers import ProductSerializer

@api_view(['GET'])
def api_home(request):

    query = BaseProduct.objects.all()
    serializer = ProductSerializer(query, many=True)
   
    return Response(serializer.data)