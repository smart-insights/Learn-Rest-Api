from django.urls import path
from . import views


urlpatterns = [
    path('products', views.get_products, name='api_get_products'),
    path('add_products', views.add_product, name='api_add_products'),
]