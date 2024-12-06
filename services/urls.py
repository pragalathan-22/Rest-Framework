from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, ServiceViewSet

# Create a router and register the viewsets
router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'services', ServiceViewSet)

urlpatterns = [
    path('api/', include(router.urls)),  # Include the router URLs
]
