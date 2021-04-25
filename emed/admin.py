from django.contrib import admin
from emed.models import UserProfileInfo
from .models import Category, Product


admin.site.register(UserProfileInfo)

admin.site.register(Category)
admin.site.register(Product)


