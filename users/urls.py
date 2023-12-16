from django.urls import path
from users.views import *

app_name = 'users'

urlpatterns = [
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', register_user, name='register'),
    path('subscribe/', subscribe, name='subscribe'),
    path('profile/', profile, name='profile')
]
