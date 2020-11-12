from django.urls import path
from catalog.views import product_list, category, product

app_name = 'catalog'
urlpatterns = [
    path('', product_list, name='product_list'),
    path('<slug:slug>/', category, name='category'),
    path('produtos/<slug:slug>', product, name='product'),
]
