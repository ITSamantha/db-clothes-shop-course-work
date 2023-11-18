from django.urls import path
from shop.views import *

app_name = 'shop'

urlpatterns = [
    path('contact/', contact, name='contact'),
    path('topic/<str:topic>', topic, name='topic'),
]
