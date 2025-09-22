from django.conf.urls import path
from . import views

urlpatterns = [
    path('', views.pub_b2b),
]
