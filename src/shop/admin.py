from django.contrib import admin
from .models import Product, Category, Order, Cart


class AdminProduct(admin.ModelAdmin):
    list_display = ("title", "category", "price", "date_added")
    
class AdminCategory(admin.ModelAdmin):
    list_display = ("name", "date")

# Register your models here.
admin.site.register(Product, AdminProduct)
admin.site.register(Category, AdminCategory)
admin.site.register(Order)
admin.site.register(Cart)