from django.urls import path
from users.views import *

app_name = 'users'

urlpatterns = [
    path('login/', LoginUserView.as_view(), name='login'),
    path('logout/', LogoutUserView.as_view(), name='logout'),
    path('register/', RegisterUserView.as_view(), name='register'),
    path('subscribe/', SubscribeView.as_view(), name='subscribe'),
    path('profile/', ProfileUserView.as_view(), name='profile')
]
