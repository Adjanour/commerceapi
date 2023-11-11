from django.db import connection
from rest_framework import serializers

from Product.models import ProductDetails

class ProductDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductDetails
        fields = '__all__'