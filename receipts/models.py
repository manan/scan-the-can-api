from django.db import models
from userprofiles.models import UserProfile
from products.models import Product
from companies.models import Company
# Create your models here.


class Receipt(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(UserProfile, related_name='receipts')
    company = models.ForeignKey(Company)

    def purchase(self, prod_id=False, barcode=False):
        prod = False
        if prod_id:
            prod = Product.objects.get(id=prod_id)
        if barcode:
            prod = Product.objects.get(barcode=barcode)
        c = Copy(name=prod.name, description=prod.description, price=prod.price, barcode=prod.barcode)
        c.receipt = self
        c.save()
        self.save()


class Copy(models.Model):
    receipt = models.ForeignKey(Receipt, related_name='products')
    name = models.CharField(max_length=100)
    description = models.TextField(default="")
    price = models.FloatField(default=0.0)
    barcode = models.CharField(max_length=200, unique=True)
