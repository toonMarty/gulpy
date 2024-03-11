"""
This module contains gulpy API serializers
"""
from rest_framework import serializers
from .models import Product, ProductVariant


class ProductBulkCreateSerializer(serializers.ListSerializer):
    """
    Serialize bulk created products and their variants
    """
    def create(self, validated_data):
        product_list = []
        variants_list = []

        for obj in validated_data:
            prod_variants = []
            for variant in obj['variants']:
                prod_variants.append(ProductVariant(**variant))
            variants_list.append(prod_variants)
            product_list.append(Product(name=obj['name'], image=obj['image']))
        products = Product.objects.bulk_create(product_list)

        variants_objs = []

        for i, prod_obj in enumerate(products):
            variants_sub_list = variants_list[i]
            for variant in variants_sub_list:
                variant.product_id = prod_obj
                variants_objs.append(variant)
        ProductVariant.objects.bulk_create(variants_objs)
        return products


class ProductVariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductVariant
        fields = ['sku', 'name', 'price', 'details']
        list_serializer_class = ProductBulkCreateSerializer


class ProductSerializer(serializers.ModelSerializer):
    variants = ProductVariantSerializer(many=True, read_only=False)

    class Meta:
        """
        serialize the Product model
        and include the following fields
        during serialization
        """
        model = Product
        fields = ['id', 'name', 'image', 'variants']
        list_serializer_class = ProductBulkCreateSerializer


