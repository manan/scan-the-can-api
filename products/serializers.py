from rest_framework import serializers
from .models import Product


class ProductExtendedSerializer(serializers.ModelSerializer):
    company_name = serializers.ReadOnlyField(source='company.name')

    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'price', 'barcode', 'quantity', 'company', 'company_name')


class ProductWriteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('name', 'description', 'price', 'barcode', 'quantity', 'company')
