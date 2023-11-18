from django.urls import path
from orders.views import *

app_name = 'orders'

urlpatterns = [
    path('cart/', cart, name='cart'),
    path('checkout/', checkout, name='checkout'),
    path('favourites/', favourites, name='favourites'),
]
