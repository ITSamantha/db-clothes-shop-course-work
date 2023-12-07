from django.contrib import admin
from users.models import *


# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    pass
