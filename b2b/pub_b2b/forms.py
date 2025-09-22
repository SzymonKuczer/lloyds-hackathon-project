from django import forms
from .models import Product_listing, Retail_listing


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product_listing
        fields = ['title', 'description']


class RetailForm(forms.ModelForm):
    class Meta:
        model = Retail_listing
        fields = ['title', 'description']
