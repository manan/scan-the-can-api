from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='profile')
    barcode = models.IntegerField(unique=True)
