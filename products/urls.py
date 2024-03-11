"""
URL patterns for the views
"""
from django.urls import path, include
from .views import ProductViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='Product')

urlpatterns = router.urls
