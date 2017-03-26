from django.shortcuts import render
from django.contrib.auth.models import User

from .permissions import IsUserOfProfile
from .models import Company

from .serializers import CompanyReadSerializer, CompanyWriteSerializer, CompanyRegistrationSerializer
from rest_framework import generics, permissions
from rest_framework.authentication import TokenAuthentication

# Create your views here.


# ['GET']
class SelfDetails(generics.RetrieveAPIView):
    model = Company
    serializer_class = CompanyReadSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = [
        permissions.IsAuthenticated,
    ]

    def get_object(self):
        return self.request.user.company


# ['POST']
class AddUser(generics.CreateAPIView):
    model = User
    serializer_class = CompanyRegistrationSerializer
    permission_classes = [
        permissions.AllowAny,
    ]


# ['POST']
class AddCompany(generics.CreateAPIView):
    model = Company
    serializer_class = CompanyWriteSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = [
        permissions.IsAuthenticated,
        IsUserOfProfile,
    ]


# ['GET']
class UserList(generics.ListAPIView):
    model = User
    queryset = User.objects.all().order_by('id')
    serializer_class = CompanyRegistrationSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = [
        permissions.IsAdminUser,
    ]


# ['GET']
class CompanyList(generics.ListAPIView):
    model = Company
    queryset = Company.objects.all().order_by('id')
    authentication_classes = (TokenAuthentication,)
    permission_classes = [
        permissions.IsAdminUser,
    ]

    def get_serializer_class(self):
        return CompanyReadSerializer
