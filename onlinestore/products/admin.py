from django.contrib import admin
from .models import *


class ProductImgInline(admin.TabularInline):
    model = ProductImg
    extra = 0


class ProductAdmin(admin.ModelAdmin):

    list_display = ['name', 'description']
    inlines = [ProductImgInline]

    class Meta:
        model = Product


class ProductImgAdmin(admin.ModelAdmin):

    list_display = ['id']

    class Meta:
        model = ProductImg



admin.site.register(Product, ProductAdmin)
admin.site.register(ProductImg, ProductImgAdmin)