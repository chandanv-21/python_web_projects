from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('student_api/', views.StudentAPI.as_view()),
    path('student_api/<int:pk>', views.StudentAPI.as_view()),
]