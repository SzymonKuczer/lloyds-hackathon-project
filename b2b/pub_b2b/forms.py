from django import forms
from .models import Product_listing


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product_listing
        fields = ['brand', 'model', 'price', 'quantity_available', 'beverage_type']
