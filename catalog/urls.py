from django.conf.urls import url
from django.urls import path, re_path
from catalog.views import product_list, category, product

app_name = 'catalog'
urlpatterns = [
    path('', product_list, name='product_list'),
    path('<slug:slug>/', category, name='category'),
    path('produtos/<slug:slug>', product, name='product'),
    # url(r'(?P<slug>[\w_-]+)/$', category, name='category')
]
