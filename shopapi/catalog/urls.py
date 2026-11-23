from os import name

from django.urls import path

from accounts.views import RegisterView
from .views import ProductListView, get_product_by_category

urlpatterns = [
    path('products', ProductListView.as_view(), name = 'product_list'),
    path('categories/<slug:slug>/',  get_product_by_category, name = 'product_list_by_category'),

]
