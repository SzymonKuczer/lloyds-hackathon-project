from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
path('choose-listing/', views.choose_listing_type, name='choose_listing'),
    path('create-product/', views.create_plisting, name='create_plisting'),
    path('create-retail/', views.create_rlisting, name='create_rlisting'),
    path('products/', views.product_listings, name='product_listing'),
    path('retail/', views.retail_listings, name='retail_listing')
]
