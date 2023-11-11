from django.shortcuts import render
from rest_framework import viewsets,authentication,permissions
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from Product.models import ProductDetails,Product
from Product.serializers import ProductDetailsSerializer

# Create your views here.

class ProductViewSet(viewsets.ModelViewSet):
    queryset = ProductDetails.objects.all()
    serializer_class = ProductDetailsSerializer
    
       
        