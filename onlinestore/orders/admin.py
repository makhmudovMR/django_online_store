from django.contrib import admin
from .models import *


class OrderAdmin(admin.ModelAdmin):
    list_display = ['customer_name', 'customer_email']

    class Meta:
        model = Order


class ProductInOrderAdmin(admin.ModelAdmin):
    # list_display = ['customer_name', 'customer_email']

    class Meta:
        model = ProductInOrder


class StatusAdmin(admin.ModelAdmin):
    # list_display = ['customer_name', 'customer_email']

    class Meta:
        model = Status



admin.site.register(Order, OrderAdmin)
admin.site.register(Status, StatusAdmin)
admin.site.register(ProductInOrder, ProductInOrderAdmin)
