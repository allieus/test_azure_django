from django.shortcuts import render
from django.views.generic import ListView
from .models import Product


product_list = ListView.as_view(model=Product)
