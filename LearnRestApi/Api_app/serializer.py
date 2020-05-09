from rest_framework import serializers
from .models import AddProduct


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddProduct
        fields = ('product_name', 'product_desc', 'product_image', )

