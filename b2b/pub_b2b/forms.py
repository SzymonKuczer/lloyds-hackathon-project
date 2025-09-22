from django import forms
from .models import Product_listing, Retail_listing


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product_listing
        fields = ['brand', 'model', 'price', 'quantity_available', 'beverage_type']


class RetailForm(forms.ModelForm):
    class Meta:
        model = Retail_listing
        fields = ['brand', 'model', '']
