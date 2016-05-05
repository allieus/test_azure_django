from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from .models import Product
from .forms import ProductForm


product_list = ListView.as_view(model=Product)

product_detail = DetailView.as_view(model=Product)

product_new = CreateView.as_view(model=Product, form_class=ProductForm)
    # success_url=reverse_lazy('shop:product_list'))

product_edit = UpdateView.as_view(model=Product, form_class=ProductForm)
