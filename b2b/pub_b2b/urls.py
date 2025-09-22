from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
<<<<<<< HEAD
path('choose-listing/', views.choose_listing_type, name='choose_listing'),
    path('create-product/', views.create_plisting, name='create_plisting'),
    path('create-retail/', views.create_rlisting, name='create_rlisting'),
    path('products/', views.product_listings, name='product_listing'),
    path('retail/', views.retail_listings, name='retail_listing')
=======


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
>>>>>>> 3d966c41b21dfa76f1520286a524206726b755d2
]
