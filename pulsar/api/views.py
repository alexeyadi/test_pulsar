from shop.models import Product
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter
from .serializers import ProductSerializer
from django_filters.rest_framework import DjangoFilterBackend


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filterset_fields = ('status', )
    search_fields = ('title', 'model_number', )
