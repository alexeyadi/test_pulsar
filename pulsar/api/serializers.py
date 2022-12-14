from rest_framework import serializers
from shop.models import Product


class ImageSerializer(serializers.Serializer):
    path = serializers.URLField(read_only=True)
    formats = serializers.ListField(read_only=True)


class ProductSerializer(serializers.ModelSerializer):
    images = ImageSerializer(read_only=True)

    class Meta:
        model = Product
        fields = ('id', 'title', 'model_number', 'price', 'status', 'images')
