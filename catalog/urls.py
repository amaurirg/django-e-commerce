from django.urls import path
from catalog.views import product_list


app_name = 'catalog'
urlpatterns = [
    path('', product_list, name='product_list'),
]