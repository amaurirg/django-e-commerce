from django.urls import path
from checkout.views import create_cartitem, cart_item


app_name = 'checkout'
urlpatterns = [
    path('carrinho/adicionar/<slug:slug>', create_cartitem, name='create_cartitem'),
    path('carrinho/', cart_item, name='cart_item')
]