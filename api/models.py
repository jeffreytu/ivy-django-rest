from django.db import models
from django.core.validators import RegexValidator

alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')

# Create your models here.
class Product(models.Model):
    sku = models.CharField(max_length=25, blank=True, null=True, validators=[alphanumeric])
    title = models.CharField(max_length=200, blank=True, null=True)
    price = models.DecimalField(blank=True, null=True, max_digits=10, decimal_places=2)
    status = models.CharField(max_length=10, blank=True, null=True)
    category = models.IntegerField(blank=True, null=True)

def __str__(self):
    return self.title