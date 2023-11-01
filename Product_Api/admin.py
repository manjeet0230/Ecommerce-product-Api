from django.contrib import admin
from .models import *

@admin.register(Product)
class Product_admin(admin.ModelAdmin):
    list_display=['id','name','description','price','image','created_at']

admin.site.register(Category)
admin.site.register(QuantityVariant)
admin.site.register(ColorVariant)

admin.site.register(SizeVariant)

admin.site.register(ProductImages)