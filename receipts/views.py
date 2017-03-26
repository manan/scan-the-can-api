from django.shortcuts import render
from rest_framework import generics
from rest_framework import permissions
from rest_framework.authentication import TokenAuthentication

from .models import Receipt

# Create your views here.


class ReceiptList(generics.ListAPIView):
    model = Receipt
    queryset = Receipt.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = [
        permissions.IsAdminUser,
    ]
