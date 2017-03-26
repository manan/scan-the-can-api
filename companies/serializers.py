from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Company
from products.serializers import ProductExtendedSerializer


class CompanyReadSerializer(serializers.ModelSerializer):
    products = ProductExtendedSerializer(many=True, read_only=True)

    class Meta:
        model = Company
        fields = ('id', 'user', 'name', 'products')


class CompanyWriteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = ('user', 'name')


class CompanyRegistrationSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email')
        write_only_fields = (['password'])

    def create(self, validated_data):
            user = User.objects.create(username=validated_data['username'],
                                       email=validated_data['email'],)
            user.set_password(validated_data['password'])
            user.save()
            return user
