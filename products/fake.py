"""
This module populates the database relations with fake data
Observes relationships and bulk creates records
"""
import faker_commerce
from random import randint
from django.db import IntegrityError
from faker import Faker
from .models import Product, ProductVariant


def products(count=10):
    """
    create fake products, append them
    to a list then perform a bulk create to the database
    :param count: the number of Product instances to add
    Initialized to 10. However, larger numbers can be passed
    """
    fake = Faker()
    prod_objs = []

    for i in range(count):
        prod_objs.append(Product(
            name=fake.word(),
            image=f'{fake.word()}.jpg'
        ))
    try:
        Product.objects.bulk_create(prod_objs, return_queryset=True)
    except IntegrityError as exc:
        raise exc


def variants(count=10):
    """
    create fake product variants, append to a list of
    ProductVariant objects then bulk create
    :param count: the number of variants to add to the database
    """
    fake = Faker()
    fake.add_provider(faker_commerce.Provider)
    variant_objs = []
    product_count = Product.objects.count()

    for i in range(count):
        p = Product.objects.get(id=randint(1, product_count - 1))
        variant_objs.append(ProductVariant(
            sku=fake.bothify(text='??######'),
            name=fake.ecommerce_name(),
            details=fake.text(),
            price=fake.pyfloat(left_digits=8, right_digits=2, positive=True, min_value=1),
            product_id=p
        ))
    try:
        ProductVariant.objects.bulk_create(variant_objs, return_queryset=True)
    except IntegrityError as exc:
        raise exc



