from django.urls import path
import products.views as views

app_name = 'products'

urlpatterns = [
    # path('product/<int:product_id>', contact, name='contact'),
    path('product_details/', views.product_details, name='product_details'),
    path('category/<str:category>', views.product_category, name='product_category'),
    path('shop/', views.shop, name='shop'),
]
