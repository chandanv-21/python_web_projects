from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('student_api/', views.student_api),
    path('student_api/<int:pk>', views.student_api),
]
