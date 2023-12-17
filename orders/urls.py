from django.urls import path
from orders.views import *

app_name = 'orders'

urlpatterns = [
    path('cart/', CartView.as_view(), name='cart'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('favourites/', FavouritesView.as_view(), name='favourites'),
    path('add_product_to_cart/', add_product_to_cart, name='add_product_to_cart')
]
