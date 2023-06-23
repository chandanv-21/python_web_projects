from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from api import views

#Creating router object
router=DefaultRouter()

# Register StudentViewSet with Router
router.register('studentapi',views.StudentViewSet, basename='student')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
