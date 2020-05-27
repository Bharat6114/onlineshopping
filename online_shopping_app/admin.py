from django.contrib import admin
from online_shopping_app.models import Products,Category
from account.models import User

# Register your models here.

@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ("product_name","product_description","product_detail" ,"product_price", "created_at")
    prepopulated_fields = {"slug": ("product_name",)}
    # readonly_fields = ("author",)
    # 
    # 
admin.site.register(Category)
admin.site.register(User)