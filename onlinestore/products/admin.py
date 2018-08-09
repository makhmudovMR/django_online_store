from django.contrib import admin
from .models import *

class ProductAdmin(admin.ModelAdmin):

    list_display = ['name', 'description']

    class Meta:
        model = Product


class ProductImgAdmin(admin.ModelAdmin):

    list_display = ['id']

    class Meta:
        model = ProductImg



admin.site.register(Product, ProductAdmin)
admin.site.register(ProductImg, ProductImgAdmin)