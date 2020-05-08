from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class AddProduct(models.Model):
    product_name = models.CharField(max_length=255, blank=True, null=True)
    product_desc = models.TextField(max_length=255, blank=True, null=True)
    product_image = models.ImageField(upload_to='products/', null=True, blank=True)