

# Create your models here.
from django.db import models


class Vendor(models.Model):
    abbreviation = models.CharField(max_length=20)
    firm_name = models.CharField(max_length=200)
    address = models.TextField()
    village = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100)
    pincode = models.CharField(max_length=10)
    email = models.EmailField()
    phone_no = models.CharField(max_length=15)
    fax_no = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.firm_name


class Item(models.Model):
    ohe_code = models.CharField(max_length=50)
    rin_no = models.CharField(max_length=50)
    description = models.TextField()
    drawing_no = models.CharField(max_length=100, blank=True)
    drawing_image = models.ImageField(upload_to='drawings/', null=True, blank=True)

    vendors = models.ManyToManyField(Vendor)

    def __str__(self):
        return self.ohe_code
