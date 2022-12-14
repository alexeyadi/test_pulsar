from rest_framework import serializers
from shop.models import Product


class ImageSerializer(serializers.Serializer):
    # products = serializers.StringRelatedField(many=True, read_only=True)
    path = serializers.URLField(source='url', read_only=True)
    formats = serializers.SerializerMethodField()

    def get_formats(self, obj):
        return [obj.primary_format, obj.image.format]


class ProductSerializer(serializers.ModelSerializer):
    images = ImageSerializer(read_only=True)

    class Meta:
        model = Product
        fields = ('id', 'title', 'model_number', 'price', 'status', 'images')


    # def create(self, validated_data):
    #     images = validated_data.pop('images')
    #     product = Product.objects.create(**validated_data)

    #     for image in images:
    #         current_image, status = Image.objects.get_or_create(
    #             **image)
    #         Image.objects.create(
    #             image=current_image, product=product)
    #     return product
