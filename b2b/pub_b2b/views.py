from django.shortcuts import render
from rest_framework import generics
from .models import (
    Retailer,
    Product,
    Supplier,
    Stock,
    Product_listing,
    Retail_listing
)
from .serializers import (
    Retailer_Serializer,
    Product_Serializer,
    Supplier_Serializer,
    Stock_Serializer,
    Product_Listing_Serializer,
    Retail_Listing_Serializer
)

# Home page view
def homepage(request):
    return render(request, '../templates/homepage.html')


# About page view
def about(request):
    return render(request, 'about.html')


# Login page view
def login(request):
    return render(request, 'login.html')


# Register page view
def register(request):
    return render(request, 'register.html')


# Optional: main index view
def pub_b2b(request):
    return render(request, 'homepage.html')

# Retailer Views
class RetailerListCreate(generics.ListCreateAPIView):
    queryset = Retailer.objects.all()
    serializer_class = Retailer_Serializer

class RetailerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Retailer.objects.all()
    serializer_class = Retailer_Serializer

# Product Views
class ProductListCreate(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = Product_Serializer

class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = Product_Serializer

# Supplier Views
class SupplierListCreate(generics.ListCreateAPIView):
    queryset = Supplier.objects.all()
    serializer_class = Supplier_Serializer

class SupplierDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Supplier.objects.all()
    serializer_class = Supplier_Serializer

# Stock Views
class StockListCreate(generics.ListCreateAPIView):
    queryset = Stock.objects.all()
    serializer_class = Stock_Serializer

class StockDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Stock.objects.all()
    serializer_class = Stock_Serializer

# Product_listing Views
class ProductListingListCreate(generics.ListCreateAPIView):
    queryset = Product_listing.objects.all()
    serializer_class = Product_Listing_Serializer

class ProductListingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product_listing.objects.all()
    serializer_class = Product_Listing_Serializer

# Retail_listing Views
class RetailListingListCreate(generics.ListCreateAPIView):
    queryset = Retail_listing.objects.all()
    serializer_class = Retail_Listing_Serializer

class RetailListingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Retail_listing.objects.all()
    serializer_class = Retail_Listing_Serializer

