from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import io
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from .models import Student
from .serializers import StudentSerializers
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def student_api(request):
    if request.method=="GET":
        json_data=request.body
        stream=io.BytesIO(json_data)
        pydata=JSONParser().parse(stream)
        id=pydata.get('id',None)
        if id is not None:
            stu=Student.objects.get(id=id)
            serializer=StudentSerializers(stu)
            json_data=JSONRenderer().render(serializer.data)
            return HttpResponse(json_data, content_type="application/json")
        stu=Student.objects.all()
        serializer=StudentSerializers(stu, many=True)
        json_data=JSONRenderer().render(serializer.data)
        return HttpResponse(json_data,content_type="application/json")

    if request.method=="POST":
        json_data=request.body
        stream=io.BytesIO(json_data)
        pydata=JSONParser().parse(stream)
        serializer=StudentSerializers(data=pydata)
        if serializer.is_valid():
            serializer.save()
            res={'msg':'Data inserted'}
            res_json=JSONRenderer().render(res)
            return HttpResponse(res_json,content_type='application/json')
        json_data=JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type='application/json')
    
    if request.method=="PUT":
        json_data=request.body
        stream=io.BytesIO(json_data)
        pydata=JSONParser().parse(stream)
        id= pydata.get('id')
        stu=Student.objects.get(id=id)
        serializer=StudentSerializers(stu, data=pydata, partial=True)
        if serializer.is_valid():
            serializer.save()
            res={'msg':'Data updated'}
            res_json=JSONRenderer().render(res)
            return HttpResponse(res_json, content_type='application/json')
        json_data=JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type='application/json')
    
    if request.method=='DELETE':
        json_data=request.body
        stream=io.BytesIO(json_data)
        pydata=JSONParser().parse(stream)
        id=pydata.get('id')
        stu=Student.objects.get(id=id)
        stu.delete()
        res={'msg':'Data Deleted'}
        # res_json=JSONRenderer().render(res)
        # return HttpResponse(res_json,content_type='application/json')
        return JsonResponse(res, safe=False)

        