from django.urls import path
import products.views as views

app_name = 'products'

urlpatterns = [
    # path('product/<int:product_id>', contact, name='contact'),
    # path('product/details/<slug:product_slug>', views.product_details, name='product_details'),
    path('product_details/<int:product_id>', views.ProductDetailView.as_view(), name='product_details'),
    path('product_details/<int:product_id>/size_details/', views.get_size_details, name='size_details'),
    path('category/<int:category>', views.product_category, name='product_category'),
    path('shop/', views.shop, name='shop'),
    path('filter_products/', views.FilterProductsView.as_view(), name='filter_products'),
]
