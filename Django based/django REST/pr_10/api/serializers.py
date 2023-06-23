from rest_framework import serializers
from api.models import Category, Item

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields=['id','name']

class ItemSerializer(serializers.ModelSerializer):
    url=serializers.HyperlinkedIdentityField(view_name='item-detail')
    class Meta:
        model=Item
        fields=['id','url','item_name','price','on_discount','discount_price','category','stock','description']