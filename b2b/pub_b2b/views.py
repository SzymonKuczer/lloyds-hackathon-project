from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


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
    products = Product_listing.objects.all().order_by('-id')
    return render(request, 'product_list.html', {'products': products})


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
        return render(request, 'rcreate_post.html', {'form': form})


def retail_listings(request):
    products = Retail_listing.objects.all().order_by('-id')
    return render(request, 'product_list.html', {'products': products})
