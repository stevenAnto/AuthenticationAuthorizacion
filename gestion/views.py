from django.shortcuts import render
from .models import Producto
from .serializers import ProductoSerializer
from rest_framework import viewsets, permissions
from .models import Producto
from .serializers import ProductoSerializer


class CustomDjangoModelPermissions(permissions.DjangoModelPermissions):
    perms_map = {
        'GET': ['%(app_label)s.view_%(model_name)s'],
        'OPTIONS': [],
        'HEAD': [],
        'POST': ['%(app_label)s.add_%(model_name)s'],
        'PUT': ['%(app_label)s.change_%(model_name)s'],
        'PATCH': ['%(app_label)s.change_%(model_name)s'],
        'DELETE': ['%(app_label)s.delete_%(model_name)s'],
    }

class ProductoViewSet(viewsets.ModelViewSet):
    permission_classes = [CustomDjangoModelPermissions]
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

    def list(self, request, *args, **kwargs):
        print("Usuario:", request.user)
        print("Está autenticado:", request.user.is_authenticated)
        print("Permisos:", request.user.get_all_permissions())
        
        # Debug específico para DjangoModelPermissions
        permission_instance = permissions.DjangoModelPermissions()
        
        print("Permisos requeridos:", permission_instance.get_required_permissions(request.method, self.queryset.model))
        print("¿Tiene permiso?:", permission_instance.has_permission(request, self))
        
        # Verificar si es superuser
        print("is_superuser:", request.user.is_superuser)
        print("is_staff:", request.user.is_staff)
    
        return super().list(request, *args, **kwargs)


    def create(self, request, *args, **kwargs):
        print("=== DEBUG CREATE PRODUCTO ===")
        print("Usuario:", request.user)
        print("Está autenticado:", request.user.is_authenticated)
        print("Permisos del usuario:", request.user.get_all_permissions())
        
        # Debug específico para DjangoModelPermissions en CREATE
        permission_instance = permissions.DjangoModelPermissions()
        
        print("Método HTTP:", request.method)
        print("Permisos requeridos para CREATE:", permission_instance.get_required_permissions(request.method, self.queryset.model))
        print("¿Tiene permiso para CREATE?:", permission_instance.has_permission(request, self))
        
        # Verificar si es superuser
        print("is_superuser:", request.user.is_superuser)
        print("is_staff:", request.user.is_staff)
        
        # Debug adicional del modelo
        print("Modelo:", self.queryset.model)
        print("App label:", self.queryset.model._meta.app_label)
        print("Model name:", self.queryset.model._meta.model_name)
        return super().create(request, *args, **kwargs)
    

