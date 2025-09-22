"""
URL configuration for b2b project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from pub_b2b import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage, name='homepage'),
    path('about/', views.about, name='about'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),

    path('api/retailers/', views.RetailerListCreate.as_view(), name='retailer-list-create'),
    path('api/retailers/<int:pk>/', views.RetailerDetail.as_view(), name='retailer-detail'),
    path('api/products/', views.ProductListCreate.as_view(), name='product-list-create'),
    path('api/products/<str:pk>/', views.ProductDetail.as_view(), name='product-detail'), # Product_id is char
    path('api/suppliers/', views.SupplierListCreate.as_view(), name='supplier-list-create'),
    path('api/suppliers/<int:pk>/', views.SupplierDetail.as_view(), name='supplier-detail'),
    path('api/stocks/', views.StockListCreate.as_view(), name='stock-list-create'),
    path('api/stocks/<int:pk>/', views.StockDetail.as_view(), name='stock-detail'),
    path('api/product_listings/', views.ProductListingListCreate.as_view(), name='product-listing-list-create'),
    path('api/product_listings/<int:pk>/', views.ProductListingDetail.as_view(), name='product-listing-detail'),
    path('api/retail_listings/', views.RetailListingListCreate.as_view(), name='retail-listing-list-create'),
    path('api/retail_listings/<int:pk>/', views.RetailListingDetail.as_view(), name='retail-listing-detail'),

    path('b2b/', include('pub_b2b.urls'))
]
