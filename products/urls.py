"""
URL patterns for the views
"""
from django.urls import path, include
from .views import ProductViewSet, ProductVariantViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='Product')
router.register(r'product-variants', ProductVariantViewSet, basename='ProductVariant')

urlpatterns = router.urls
