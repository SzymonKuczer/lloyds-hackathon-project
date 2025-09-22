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


class  Product(models.Model):
    Product_id = models.CharField(max_length=6, primary_key = True)

    Product_name = models.CharField(max_length=255)
    Product_Storage_CHOICES = [
        ('Barrel', 'BARREL'),
        ('Bottle', 'BOTTLE'),
        ('Crate', 'CRATE'),
    ]
    storage_type = models.CharField(max_length=20, choices=Product_Storage_CHOICES)
    Product_TYPE_CHOICES = [
        ('Lager', 'LAGER'),
        ('Cider', 'CIDER'),
        ('Stout', 'STOUT'),
        ('Ale', 'ALE'),
    ]
    product_type = models.CharField(max_length=20, choices=Product_TYPE_CHOICES)
    pass

class Supplier(models.Model):
    supplier_account_id = models.AutoField(primary_key=True) # Auto-incrementing integer PK

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

class Stock(models.Model):
    stock_id = models.AutoField(primary_key=True)  # Auto-incrementing integer PK
    retailer_account_id = models.ForeignKey(Retailer, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)

    beverage_name = models.CharField(max_length=255)
    pass

class Product_listing(models.Model):
    p_listing_id = models.AutoField(primary_key=True)  # Auto-incrementing integer PK
    supplier_account_id = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)

    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity_available = models.IntegerField()
    beverage_name = models.CharField(max_length=255)
    beverage_type = models.CharField(max_length=255)
    pass