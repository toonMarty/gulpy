from django.utils.functional import cached_property
from rest_framework import serializers
from .models import Product, ProductVariant
from django.db import transaction, IntegrityError


class ProductBulkCreateSerializer(serializers.ListSerializer):
    def create(self, validated_data):
        prod_data = [Product(**prod_instance) for prod_instance in validated_data]
        return Product.objects.bulk_create(prod_data)


class ProductVariantBulkCreateSerializer(serializers.ListSerializer):
    @transaction.atomic
    def create(self, validated_data):
        """
        bulk_create product variants
        """
        variants_list = []
        for data in validated_data:
            product_id = data.pop('product_id')
            name = product_id.name
            image = product_id.image
            product_obj = Product.objects.create(name=name, image=image)
            variants_list.append(ProductVariant(**{**data, **{'product_id': product_obj}}))
        # variant_data = [ProductVariant(**variant_instance) for variant_instance in validated_data]
        return ProductVariant.objects.bulk_create(variants_list)


class ProductVariantSerializer(serializers.ModelSerializer):
    class Meta:
        """
        serialize the ProductVariant model
        """
        model = ProductVariant
        fields = ['sku', 'name', 'price', 'details', 'product_id']
        list_serializer_class = ProductVariantBulkCreateSerializer

    def create(self, validated_data):
        """
        Link a product to its variants
        :param validated_data: request data passed as json
        :return: an instance of a product variant
        """
        product_id = validated_data.pop('product_id')
        name = product_id.name
        image = product_id.image

        if not name and image:
            raise serializers.ValidationError('product not found')
        product_obj = Product.objects.create(name=name, image=image)
        validated_data.update({'product_id': product_obj})
        return ProductVariant.objects.create(**validated_data)


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

