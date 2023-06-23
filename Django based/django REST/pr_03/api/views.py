from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer

# Create your views here.
@api_view(['GET','POST'])
def student_api(request):
    if request.method == 'GET':
        id =request.data.get('id')
        print(id)
        if id is not None:
            stu=Student.objects.get(id=id)
            serializer=StudentSerializer(stu)
            return Response(serializer.data)
        stu=Student.objects.all()
        serializer=StudentSerializer(stu, many=True)
        return Response(serializer.data)

    if request.method=='POST':
        print(request.data)
        return Response({'msg':'This is POST request'})
       
