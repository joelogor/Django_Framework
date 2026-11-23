from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .serializers import ProductSerializer, CategorySerializer
from .models import Product, Category


# Create your views here.

class ProductListView(ListAPIView):
    queryset = Product.objects.all().filter(is_active=True)
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]

# class CategoryListView(RetrieveAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer


# @api_view(['GET'])
# def product_list(request):
#     products = Product.objects.all().filter(is_active=True)
#     serializer = ProductSerializer(products, many=True)
#     return Response(serializer.data, status=status.HTTP_200_OK)
@api_view(['Get'])
@permission_classes([AllowAny])
def get_product_by_category(request, slug):
    try:
        category = Category.objects.get(slug=slug)
        serializer = CategorySerializer(category)
        return Response(serializer.data)

    except Category.DoesNotExist:
        return Response({"Error":"Category not found"},status=status.HTTP_404_NOT_FOUND)

