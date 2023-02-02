from django.db import models
import  datetime

# Create your models here.
class Department(models.Model):
    name=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Role(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Employee(models.Model):
    f_name=models.CharField(max_length=100,null=False)
    l_name=models.CharField(max_length=100,null=False)
    dept=models.ForeignKey(Department, on_delete=models.CASCADE)
    phone=models.IntegerField(default=0)
    salary=models.IntegerField(default=0)
    bonus=models.IntegerField(default=0)
    role=models.ForeignKey(Role,on_delete=models.CASCADE)
    dt_of_join=models.DateField(default=datetime.date.today)
    def __str__(self):
        return "%s %s %s" %( self.f_name, self.l_name, self.role.name)
