from django.shortcuts import render
from .models import Producto
from .serializers import ProductoSerializer
from rest_framework import viewsets, permissions

from rest_framework import viewsets, permissions
from .models import Producto
from .serializers import ProductoSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    permission_classes = [permissions.IsAuthenticated, permissions.DjangoModelPermissions]

