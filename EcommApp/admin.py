from django.contrib import admin
from . models import Product,CartItem,Order
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
  list_display = ["product_id","product_name","category","price","proImage"]
  
admin.site.register(Product,ProductAdmin)

class CartAdmin(admin.ModelAdmin):
  list_display = ["product_id","quantity","date_added"]

admin.site.register(CartItem,CartAdmin)


class OrderAdmin(admin.ModelAdmin):
  list_display = ["order_id","product_id","quantity","user","is_completed"]

admin.site.register(Order,OrderAdmin)