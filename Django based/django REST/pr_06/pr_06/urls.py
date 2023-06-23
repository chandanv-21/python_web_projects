from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('student_api/', views.StudentList.as_view()),
    # path('student_api/', views.StudentCreate.as_view()),
    # path('student_api/<int:pk>', views.StudentRetrieve.as_view()),
    # path('student_api/<int:pk>', views.StudentUpdate.as_view()),
    path('student_api/<int:pk>', views.StudentDestroy.as_view()),

]