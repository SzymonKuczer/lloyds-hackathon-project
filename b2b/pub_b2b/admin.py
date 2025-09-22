from django.contrib import admin
from .models import Retailer, Product, Supplier, Stock, Product_listing, Retail_listing

admin.site.register(Retailer)
admin.site.register(Product)
admin.site.register(Supplier)
admin.site.register(Stock)
admin.site.register(Product_listing)
admin.site.register(Retail_listing)
