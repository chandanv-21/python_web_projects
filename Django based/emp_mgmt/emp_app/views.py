from django.shortcuts import render, redirect,HttpResponse
from .models import Employee,Department,Role
import json
from django.db.models import Q

# Create your views here.
def index(request):
    return  render( request, 'index.html')
def all_emps(request):
    emps=Employee.objects.all()
    data={
        'emps':emps
    }
    return  render( request, 'all_emps.html',data)

def remove_emp(request):
    emps = Employee.objects.all()
    data = {
        'emps': emps
    }
    return  render( request, 'remove_emp.html', data)

def del_emp(request,emp_id=0):
    if emp_id:
        emp_to_remove=Employee.objects.filter(id=emp_id)
        emp_to_remove.delete()
        print(emp_id,type(emp_id))
        return redirect("/remove_emp")
def add_emp(request):
    if request.method=="POST":
        fname=request.POST.get("fname")
        lname=request.POST.get("lname")
        dept=request.POST.get("dept")
        location=request.POST.get("location")
        phone=request.POST.get("phone")
        salary=int(request.POST.get("salary"))
        bonus=int(request.POST.get("bonus"))
        role=request.POST.get("role")
        dt_of_join=request.POST.get("doj")
        print(fname,lname, dept, location,role, phone, salary, bonus, dt_of_join)
        entry=Employee(f_name=fname,l_name=lname, dept_id=dept, phone= phone,salary= salary, bonus= bonus,role_id= role, dt_of_join=dt_of_join)
        entry.save()
        return redirect("/add_emp")


    dept=Department.objects.all()
    locs={}
    roles = Role.objects.all()
    for dep in dept:
        locs.update({dep.id:dep.location})
    context={
        "roles": roles,
        "dept":dept,
        "locs":json.dumps(locs, default=str)

    }
    return  render( request, 'add_emp.html',context)

def update_emp(request):
    return  render( request, 'update_emp.html')
def filter_emp(request):
    if request.method=="POST":
        name=request.POST.get("name")
        dept=request.POST.get("dept")
        print(dept)
        role=request.POST.get("role")
        print(role)
        emps1=Employee.objects.all()
        if name:
            emps=emps1.filter(Q(f_name__icontains=name) | Q(l_name__icontains=name))
        if dept:
            emps=emps1.filter(dept__name__icontains=dept)
            print("dept emps",emps)
        if role:
            emps=emps1.filter(role__name__icontains=role)
            print("role emps",emps)
        context={
            "emps":emps
        }
        return render(request, "all_emps.html", context)



    return  render( request, 'filter_emp.html')
