from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('student_api/', views.StudentCreate_n_List.as_view()),
    path('student_api/<int:pk>', views.StudentRetUpdtDlt.as_view()),
]