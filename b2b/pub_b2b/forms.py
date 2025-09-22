from django import forms
from .models import Product_listing, Retail_listing

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product_listing
        fields = [
            'supplier_account_id',
            'product_id',
            'price',
            'quantity_available',
            'beverage_name',
            'beverage_type',
        ]

class RetailForm(forms.ModelForm):
    class Meta:
        model = Retail_listing
        fields = [
            'retailer_account_id',
            'product_id',
            'price',
            'beverage_name',
            'beverage_type',
        ]