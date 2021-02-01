from django.urls import path

from . import views

urlpatterns=[
path('',views.index,name='index'),
path('index.html',views.index,name='index'),
path('products.html',views.products,name='products'),
path('account.html',views.account,name='account'),
path('cart.html',views.cart,name='cart')

]