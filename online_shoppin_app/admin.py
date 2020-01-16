from django.contrib import admin
from online_shoppin_app.models import Product,Category

# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("product_name", "product_price", "created_at")
    prepopulated_fields = {"slug": ("title",)}
    # readonly_fields = ("author",)
    # 
    # 
admin.site.register(Category)