from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.product_list, name='product_list'),
    url(r'^new/$', views.product_new, name='product_new'),
]
