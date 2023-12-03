from django.contrib import admin
from shop.models import *


class CountryCityInline(admin.TabularInline):
    model = CountryCity
    extra = 1
