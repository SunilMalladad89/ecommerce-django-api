from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import api_views

# Create router
router = DefaultRouter()

# Register ViewSets
router.register('products', api_views.ProductViewSet)
router.register('categories', api_views.CategoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('register/', api_views.RegisterAPIView.as_view(), name='api-register'),
]