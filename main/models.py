from django.db import models
from django.urls import reverse


class Product(models.Model):
    product_code = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    supplier_name = models.ForeignKey('Supplier', on_delete=models.CASCADE)
    price = models.FloatField()

    def __str__(self):
        return self.product_code + ' ' + self.name

    def get_absolute_url(self):
        return reverse('main-database')


class Supplier(models.Model):
    supplier_name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.supplier_name

    def get_absolute_url(self):
        return reverse('main-database')