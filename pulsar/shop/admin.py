from django.contrib import admin
from .models import Product, Image


class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'model_number', 'price', 'status', )


class ImageAdmin(admin.ModelAdmin):
    list_display = ('old_image', )


admin.site.register(Product, ProductAdmin)
admin.site.register(Image, ImageAdmin)
