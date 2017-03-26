from django.shortcuts import render
from rest_framework import generics
from rest_framework import permissions
from rest_framework.authentication import TokenAuthentication

from .serializers import ProductExtendedSerializer, ProductWriteSerializer
from .models import Product
from .permissions import IsCompany

# Create your views here.


class ProductList(generics.ListAPIView):
    model = Product
    serializer_class = ProductExtendedSerializer
    queryset = Product.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = [
        permissions.IsAdminUser,
    ]


class AddProduct(generics.CreateAPIView):
    model = Product
    serializer_class = ProductWriteSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = [
        permissions.IsAdminUser,
        IsCompany,
    ]
