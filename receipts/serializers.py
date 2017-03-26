from rest_framework import serializers
from .models import Receipt, Copy
from products.serializers import ProductExtendedSerializer


class CopiesExtendedSerializer(serializers.ModelSerializer):

    class Meta:
        model = Copy
        fields = ('id', 'name', 'description', 'price', 'barcode')


class ReceiptReadSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source='owner.user.username')
    company_name = serializers.ReadOnlyField(source='company.name')
    products = CopiesExtendedSerializer(many=True, read_only=True)

    class Meta:
        model = Receipt
        fields = ('id', 'owner', 'username', 'date', 'products', 'company', 'company_name')


class ReceiptWriteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Receipt
        fields = ('id', 'owner', 'products', 'company')
