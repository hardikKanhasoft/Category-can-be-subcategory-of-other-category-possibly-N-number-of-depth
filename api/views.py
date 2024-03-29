from .models import Category
from .serializers import CategorySerializer
from rest_framework import viewsets

class CategoryModelViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

