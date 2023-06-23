
from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from api import views

# Initialize Router for urls;
router=DefaultRouter()
router.register('category',views.CategoryViewSet, basename='category')
router.register('item',views.ItemViewSet, basename='item')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
