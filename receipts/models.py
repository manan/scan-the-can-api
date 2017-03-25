from django.db import models
from userprofiles.models import UserProfile
from products.models import Product
from companies.modles import Company
# Create your models here.


class Receipt(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(UserProfile, related_name='receipts')
    products = models.ManyToManyField(Product)
    company = models.ForeignKey(Company)