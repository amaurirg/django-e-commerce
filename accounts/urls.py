from django.urls import path, re_path

from accounts.views import register
from catalog.views import product_list, category, product

app_name = 'accounts'
urlpatterns = [
    path('registro/', register, name='register'),
]
