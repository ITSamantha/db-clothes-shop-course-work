from django.contrib import admin
from products.models import *

# Register your models here.
admin.site.register(Category)
admin.site.register(Gender)
admin.site.register(Size)
admin.site.register(Color)
admin.site.register(CategoryGender)
admin.site.register(Product)
admin.site.register(ProductSizeColor)
admin.site.register(ProductSizeColorCount)
admin.site.register(ProductImage)
admin.site.register(ProductCategoryGender)

