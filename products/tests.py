from django.test import TestCase
from .models import Product

# Create your tests here.


class ProdModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.prod = Product.objects.create(name='abc', image='def.jpg')

    def test_prod_count(self):
        self.assertEqual(Product.objects.count(), 1)

    def test_str_rep_method(self):
        self.assertEqual(str(self.prod), 'abc')

