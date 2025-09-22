from django.db import models

# Create your models here.

class Retailer(models.Model):
    retailer_account_id = models.AutoField(primary_key=True)  # Auto-incrementing integer PK
    name = models.CharField(max_length=255)
    address = models.TextField()
    contact_email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    password = models.TextField(max_length=255)
    ACCOUNT_TYPE_CHOICES = [
        ('pub', 'Pub'),
        ('restaurant', 'Restaurant'),
        ('cafe', 'Cafe'),
        ('bar', 'Bar'),
    ]
    account_type = models.CharField(max_length=20, choices=ACCOUNT_TYPE_CHOICES)
    pass

class Supplier(models.Model):
    supplier_account_id = models.AutoField(primary_key=True)  # Auto-incrementing integer PK
    name = models.CharField(max_length=255)
    address = models.TextField()
    contact_email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    password = models.TextField(max_length=255)
    ACCOUNT_TYPE_CHOICES = [
        ('brewery', 'Brewery'),
        ('bakery', 'Bakery'),
        ('Butchers', 'Butchers'),
    ]
    account_type = models.CharField(max_length=20, choices=ACCOUNT_TYPE_CHOICES)
    pass