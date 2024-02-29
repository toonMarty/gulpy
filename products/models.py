"""
Define Models
"""
from bulkmodel.models import BulkModel
from django.db import models

# Create your models here.


class Product(BulkModel):
    """
    Define a Product
    """
    name = models.CharField(max_length=64)
    image = models.CharField(max_length=255)

    def __str__(self):
        """

        :return: a string representation of a
        product instance
        """
        return self.name


class ProductVariant(BulkModel):
    """
    Define a product variant
    """
    sku = models.CharField(max_length=128)
    name = models.CharField(max_length=64)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    details = models.CharField(max_length=255)
    product_id = models.ForeignKey(Product, related_name='variants',
                                   on_delete=models.CASCADE)

    def __str__(self):
        """
        :return: a string representation of a
        product variant instance
        """
        return self.name


