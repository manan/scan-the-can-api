from django.contrib.auth.models import User
from rest_framework import serializers
from .models import UserProfile
from receipts.serializers import ReceiptReadSerializer


class UserProfileReadSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source='user.username')
    first_name = serializers.ReadOnlyField(source='user.first_name')
    last_name = serializers.ReadOnlyField(source='user.last_name')
    receipts = ReceiptReadSerializer(many=True, read_only=True)

    class Meta:
        model = UserProfile
        fields = ('user', 'username', 'first_name', 'last_name', 'receipts', 'id')


class UserProfileCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('user',)


class ProfileRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email', 'first_name', 'last_name')
        write_only_fields = (['password'])
        read_only_fields = (['id'])

    def create(self, validated_data):
            user = User.objects.create(username=validated_data['username'],
                                       email=validated_data['email'],
                                       first_name=validated_data['first_name'],
                                       last_name=validated_data['last_name'])
            user.set_password(validated_data['password'])
            user.save()
            return user
