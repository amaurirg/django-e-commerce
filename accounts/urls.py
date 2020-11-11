from django.urls import path, re_path

from accounts.views import register, index, update_user, update_password
from catalog.views import product_list, category, product

app_name = 'accounts'
urlpatterns = [
    path('', index, name='index'),
    path('registro/', register, name='register'),
    path('alterar-senha/', update_password, name='update_password'),
    path('alterar-dados/', update_user, name='update_user'),
]
