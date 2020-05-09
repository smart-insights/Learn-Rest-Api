from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.status import HTTP_401_UNAUTHORIZED, HTTP_200_OK, HTTP_404_NOT_FOUND, HTTP_400_BAD_REQUEST
import requests

# import models
from .models import Products

# import serializers
from .serializer import ProductSerializer

# Create your views here.


@api_view(["GET"])
def get_products(request):
    try:
        products = Products.objects.all()
        items = ProductSerializer(products, many=True)
        return Response(data={"status": "Success", "message": "Products Found", "data": {"user": items.data}},
                        status=HTTP_200_OK)
    except Exception as e:
        return Response(data={"status": "Error", "message": "Get Products Failed", "data": {"errors": str(e)}},
                        status=HTTP_404_NOT_FOUND)


@api_view(["POST", ])
def add_product(request):
    if request.method == "POST":
        try:
            serializer = ProductSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
            return Response(serializer.data)
        except Exception as e:
            return Response(data={"status": "Error", "message": "No Products", "data": {"error": str(e)}}, status=HTTP_200_OK)