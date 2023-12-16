from django.urls import path
from orders.views import *

app_name = 'orders'

urlpatterns = [
    path('cart/', cart, name='cart'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('favourites/', FavouritesView.as_view(), name='favourites'),
]
