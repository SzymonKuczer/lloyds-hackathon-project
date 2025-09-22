from rest_framework import serializers
from .models import Retailer
from .models import Product
from .models import Product_listing
from .models import Retail_listing
from .models import Stock
from .models import Supplier



class Retailer_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Retailer
        fields = '__all__'

class Product_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class Product_Listing_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Product_listing
        fields = '__all__'

class Retail_Listing_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Retail_listing
        fields = '__all__'

class Stock_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = '__all__'

class Supplier_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = '__all__'
