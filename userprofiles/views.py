from django.shortcuts import render
from django.contrib.auth.models import User

from .permissions import IsUserOfProfile
from .models import UserProfile

from .serializers import UserProfileReadSerializer, ProfileRegistrationSerializer, UserProfileCreateSerializer
from rest_framework import generics, permissions
from rest_framework.authentication import TokenAuthentication

# Create your views here.


# ['GET']
class SelfDetails(generics.RetrieveAPIView):
    model = UserProfile
    serializer_class = UserProfileReadSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = [
        permissions.IsAuthenticated,
    ]

    def get_object(self):
        return self.request.user.profile


# ['POST']
class AddUser(generics.CreateAPIView):
    model = User
    serializer_class = ProfileRegistrationSerializer
    permission_classes = [
        permissions.AllowAny,
    ]


# ['POST']
class AddProfile(generics.CreateAPIView):
    model = UserProfile
    serializer_class = UserProfileCreateSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = [
        permissions.IsAuthenticated,
        IsUserOfProfile,
    ]


# ['GET']
class UserList(generics.ListAPIView):
    model = User
    queryset = User.objects.all().order_by('id')
    serializer_class = ProfileRegistrationSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = [
        permissions.IsAdminUser,
    ]


# ['GET']
class ProfileList(generics.ListAPIView):
    model = UserProfile
    queryset = UserProfile.objects.all().order_by('id')
    authentication_classes = (TokenAuthentication,)
    permission_classes = [
        permissions.IsAdminUser,
    ]

    def get_serializer_class(self):
        return UserProfileReadSerializer
