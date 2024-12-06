from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import Category, Service
from .serializers import CategorySerializer, ServiceSerializer

# CategoryViewSet to handle Category operations
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    # Custom destroy method to delete a Category
    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()  # Get the category object by ID
            instance.delete()  # Delete the category
            return Response({"message": "Category deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

# ServiceViewSet to handle Service operations
class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
