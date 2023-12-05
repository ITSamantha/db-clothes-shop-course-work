from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from products.views import index
from store import settings
from shop.views import page_not_found

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('shop/', include('shop.urls', namespace='shop')),
    path('products/', include('products.urls', namespace='products')),
    path('orders/', include('orders.urls', namespace='orders')),
    path('users/', include('users.urls', namespace='users')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [path('__debug__/', include(debug_toolbar.urls)), ] + urlpatterns

# Errors

handler404 = page_not_found

admin.site.site_header = "Cute&Classy - Administrator Panel"
admin.site.index_title = "Tables and lists"
