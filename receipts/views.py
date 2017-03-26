from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics
from rest_framework import permissions
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes

from .serializers import ReceiptReadSerializer, ReceiptWriteSerializer
from .models import Receipt

# Create your views here.


class ReceiptList(generics.ListAPIView):
    model = Receipt
    queryset = Receipt.objects.all()
    serializer_class = ReceiptReadSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = [
        permissions.IsAdminUser,
    ]


class AddReceipt(generics.CreateAPIView):
    model = Receipt
    serializer_class = ReceiptWriteSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = [
        permissions.IsAuthenticated,
    ]


@csrf_exempt
@api_view(['GET'])
@authentication_classes((TokenAuthentication,))
@permission_classes((permissions.IsAuthenticated,))
def add_products(request, rec_id, barcodes):
    receipt = Receipt.objects.get(pk=rec_id)
    barcode_list = barcodes.replace(' ', '').split(',')
    for every_barcode in barcode_list:
        receipt.purchase(barcode=every_barcode)
    serializer = ReceiptReadSerializer(receipt)
    return JsonResponse(serializer.data)
