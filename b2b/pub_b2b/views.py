
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

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



# Form request for posts
from .forms import ProductForm, RetailForm
from .models import Product_listing, Retail_listing


def choose_listing_type(request):
    if request.method == 'POST':
        listing_type = request.POST.get('listing_type')
        if listing_type == 'product':
            return redirect('create_plisting')
        elif listing_type == 'retail':
            return redirect('create_rlisting')
    return render(request, 'pub_b2b/choose_listing_type.html')


@login_required
def create_plisting(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('product_listing')
        else:
            form = ProductForm()
        return render(request, 'pcreate_post.html', {'form': form})


def product_listings(request):
    products = Product_listing.objects.all().order_by('-price')
    return render(request, 'pub_b2b/product_list.html', {'products': products})


@login_required
def create_rlisting(request):
    if request.method == 'POST':
        form = RetailForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('retail_listing')
        else:
            form = RetailForm()
        return render(request, 'pub_b2b/rcreate_post.html', {'form': form})


def retail_listings(request):
    products = Retail_listing.objects.all().order_by('-price')
    return render(request, 'pub_b2b/choose_listing_type.html', {'products': products})

    products = Retail_listing.objects.all().order_by('-id')
    return render(request, 'product_list.html', {'products': products})


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




