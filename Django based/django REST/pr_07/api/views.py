from .models import Student
from .serializers import StudentSerializer
from rest_framework.mixins import ListModelMixin, CreateModelMixin, UpdateModelMixin,RetrieveModelMixin, DestroyModelMixin
from rest_framework.generics import GenericAPIView


# List and Create - PK not required
class StudentCreate_n_List(GenericAPIView, ListModelMixin, CreateModelMixin):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

    def get(self,request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self,request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    

# Retrieve, Update and Delete- pk required
class StudentRetUpdtDlt(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

    def get(self,request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    

    def put(self,request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    

    def delete(self,request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    
#hrd@cabconindia.com