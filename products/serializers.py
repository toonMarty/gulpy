from django.core.exceptions import ValidationError
from django.db import IntegrityError
from rest_framework import serializers, pagination
from rest_framework.response import Response
from .models import Product, ProductVariant


class ProductBulkCreateSerializer(serializers.ListSerializer):
    def create(self, validated_data):
        prod_data = [Product(**prod_instance) for prod_instance in validated_data]
        return Product.objects.bulk_create(prod_data)


class ProductVariantBulkCreateSerializer(serializers.ListSerializer):
    def create(self, validated_data):
        """
        bulk_create product variants
        """
        variant_data = [ProductVariant(**instance) for instance in validated_data]
        # print(variant_data)
        return Product.objects.bulk_create(variant_data)


class ProductVariantSerializer(serializers.ModelSerializer):


    class Meta:
        """
        serialize the ProductVariant model
        """
        model = ProductVariant
        fields = ['sku', 'name', 'price', 'details']
        list_serializer_class = ProductVariantBulkCreateSerializer


class ProductSerializer(serializers.ModelSerializer):
    variants = ProductVariantSerializer(many=True, read_only=True)

    class Meta:
        """
        serialize the Product model
        and include the following fields
        during serialization
        """
        model = Product
        fields = ['id', 'name', 'image', 'variants']
        list_serializer_class = ProductBulkCreateSerializer
