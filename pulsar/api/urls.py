from django.urls import path, include
from api.views import ProductViewSet
from rest_framework import routers


v1_router = routers.DefaultRouter()
v1_router.register(r'products', ProductViewSet)

app_name = 'shop'

urlpatterns = [
    path('', include(v1_router.urls)),
]
