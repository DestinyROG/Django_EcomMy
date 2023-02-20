from django.contrib import admin
from NewApp.models import *

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=[
        'id',
        'name',
        'image',
    ]    


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display=[
        'id',
        'category',
        'name',
    ]

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display=[
        'id',
        'name',
        'quantity',
        'user',
    ]

@admin.register(Banner_image)
class Banner_imageAdmin(admin.ModelAdmin):
    list_display=[
        'id',
        'category',
        'banner_image',
        'status',
    ]