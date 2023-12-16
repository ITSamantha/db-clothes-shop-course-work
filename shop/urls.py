from django.urls import path
from shop.views import *

app_name = 'shop'

urlpatterns = [
    path('contact/', ContactView.as_view(), name='contact'),
    path('topic/<str:topic>', TopicView.as_view(), name='topic'),
]
