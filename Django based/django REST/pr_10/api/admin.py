from django.contrib import admin
from api.models import Category,Item

# Register your models here.
@admin.register(Category)
class  CategoryAdmin(admin.ModelAdmin):
    list_display=['id','name']

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display=['id','item_name', 'price', 'category', 'stock']
