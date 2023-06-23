from django.shortcuts import render
from api.models import Category, Item
from api.serializers import CategorySerializer, ItemSerializer
from rest_framework import viewsets
# Create your views here.

class CategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows category to be viewed or edited.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ItemViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows items to be viewed or edited.
    """
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
