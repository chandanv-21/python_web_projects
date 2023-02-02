from flask import Flask,session,render_template,redirect,request
import json
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, date,time


app=Flask(__name__)
with open ('config.json','r') as c:
    params=json.load(c)["param"]

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:admin@localhost/managepark"
app.config['SECRET_KEY']="some secret key"

db=SQLAlchemy(app)


class Employee(db.Model):
    sl = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=False)
    phone = db.Column(db.String(25), unique=True)
    password = db.Column(db.String(500), unique=False)
    address = db.Column(db.String(500), unique=False)
    joindate = db.Column(db.String(500), unique=False)
    status = db.Column(db.String(500), unique=False)
    updates=db.relationship('Task',backref='employee', lazy=True)
    attendances=db.relationship('Attendance',backref='employee', lazy=True)


class Task(db.Model):
    sl = db.Column(db.Integer, primary_key=True)
    task_id = db.Column(db.Integer, db.ForeignKey('employee.sl')) 
    name = db.Column(db.String(50), unique=False)
    taskname = db.Column(db.String(50), unique=False)
    starttime = db.Column(db.String(25), unique=True)
    endtime = db.Column(db.String(500), unique=False)
    tdate= db.Column(db.String(500), unique=False)
    taskstatus= db.Column(db.String(500), unique=False)
    competiondate= db.Column(db.String(500), unique=False)
    completiontime= db.Column(db.String(500), unique=False)
    

class Attendance(db.Model):
    sl = db.Column(db.Integer, primary_key=True)
    atten_id = db.Column(db.Integer, db.ForeignKey('employee.sl'))
    name = db.Column(db.String(50), unique=False)
    attendate = db.Column(db.String(500), unique=False)
    attenstatus = db.Column(db.String(500), unique=False)

    
@app.route("/",methods=["GET","POST"])
def index():
    if 'user' in session and session['user'] == params["admin_email"]:
        users=Employee.query.filter_by(status='active').all()
        return render_template("index.html",users=users)
    if request.method == 'POST':
        usermail=request.form.get("email")
        userpass = request.form.get('password')
        if (usermail == params["admin_email"]) and (userpass == params["admin_password"]):
            session['user'] = usermail
            users=Employee.query.filter_by(status='active').all()
            return render_template("index.html",users=users)
    return render_template("login.html")

@app.route("/add",methods=["GET","POST"])
def add():
    if 'user' in session and session['user'] == params["admin_email"]:
        return render_template("addStaff.html")
    redirect("/")



@app.route("/addStaff",methods=["GET","POST"])
def addStaff():
    if 'user' in session and session['user'] == params["admin_email"]:
        
        name=request.form.get("name")
        phone=request.form.get("phone")
        password=request.form.get("password")
        joindate=request.form.get("joindate")
        address=request.form.get("address")
        status='active'
        
        if request.method=="POST":
            entry=Employee(name=name, phone=phone, password =password, joindate=joindate, address=address, status=status)
            db.session.add(entry)
            db.session.commit()
            return redirect("/add")
    return redirect("/")     
@app.route("/staffList",methods=["GET","POST"])
def staffList():
    if 'user' in session and session['user'] == params["admin_email"]:
        users=Employee.query.filter_by(status='active').all()
        nusers=Employee.query.filter_by(status='deleted').all()
        return render_template("staffList.html",users=users, nusers=nusers)
    
@app.route("/activeEmployeeList",methods=["GET","POST"])
def activeStaffList():
    if 'user' in session and session['user'] == params["admin_email"]:
        users=Employee.query.filter_by(status='active').all()
        return render_template("activeStaffList.html",users=users)


@app.route("/editStaff/<int:sl>",methods=["GET","POST"])
def editStaff(sl):
    if 'user' in session and session['user'] == params["admin_email"]:
        name=request.form.get("name")
        phone=request.form.get("phone")
        password=request.form.get("password")
        joindate=request.form.get("joindate")
        address=request.form.get("address")
        status='active'
        
        if request.method=="POST":
            data=Employee.query.filter_by(sl=sl).first()
            data.name=name
            data.phone=phone
            data.password=password
            data.joindate=joindate
            data.address=address   
            db.session.commit()
            return redirect("/activeEmployeeList")
        data=Employee.query.filter_by(sl=sl).first()
        return render_template("editStaff.html", data=data,sl=sl)
    return redirect("/")

@app.route("/delete/<int:sl>",methods=["GET","POST"])
def delete(sl):
    if 'user' in session and session['user'] == params["admin_email"]:
        data=Employee.query.filter_by(sl=sl).first()
        data.status="deleted"
        db.session.add(data)
        db.session.commit()
        return redirect("/staffList")
    return redirect("/")

@app.route("/restore/<int:sl>",methods=["GET","POST"])
def restore(sl):
    if 'user' in session and session['user'] == params["admin_email"]:
        data=Employee.query.filter_by(sl=sl).first()
        data.status="active"
        db.session.add(data)
        db.session.commit()
        return redirect("/staffList")
    return redirect("/")

@app.route("/addroutine/<int:sl>",methods=["GET","POST"])
def addroutine(sl):
    if 'user' in session and session['user'] == params["admin_email"]:
        data=Employee.query.filter_by(sl=sl).first()
        if request.method=="POST":
            taskname1=request.form.get("taskname1")
            starttime1=request.form.get("starttime1")
            endtime1=request.form.get("endtime1")

            taskname2=request.form.get("taskname2")
            starttime2=request.form.get("starttime2")
            endtime2=request.form.get("endtime2")

            taskname3=request.form.get("taskname3")
            starttime3=request.form.get("starttime3")
            endtime3=request.form.get("endtime3")
            name=data.name
            task_id=data.sl
            tdate=date.today()
            entry1=Task(name=name, task_id=task_id, taskname=taskname1, starttime=starttime1, endtime=endtime1,tdate=tdate)
            entry2=Task(name=name, task_id=task_id, taskname=taskname2, starttime=starttime2, endtime=endtime2,tdate=tdate)
            entry3=Task(name=name, task_id=task_id, taskname=taskname3, starttime=starttime3, endtime=endtime3,tdate=tdate)
            if taskname1!="":
                db.session.add(entry1)
                db.session.commit()
            if taskname2!="":
                db.session.add(entry2)
                db.session.commit()
            if taskname3!="":
                db.session.add(entry3)
                db.session.commit()
            return redirect(f"/addroutine/{sl}")

    return render_template("addroutine.html",data=data, sl=sl)

@app.route("/adminattend",methods=["GET","POST"])
def adminattend():
    if 'user' in session and session['user'] == params["admin_email"]:
        datas=db.session.query(Employee, Task).join(Task).filter(Employee.status=='active', Task.taskstatus!=None)
        
        return render_template("adminattand.html", datas=datas)
    return redirect('/')



@app.route("/logout")
def logout():
    session.pop('user')
    return redirect('/')

@app.route("/emp", methods=["GET","POST"])
def emp():
    if 'user2' in session:
        users=Employee.query.filter_by(status='active',sl=int(session['user2'])).all()
        for user in users:
            details=Employee.query.filter_by(status='active').all()
            tasks=Task.query.filter_by(task_id=int(session['user2']),taskstatus=None).all()
            return render_template("dashboard.html",details=details, tasks=tasks, userid=session['user2'])

    if request.method == 'POST':    
        userid=request.form.get("userid")
        userpass = request.form.get('password')
        users=Employee.query.filter_by(status='active',sl=userid).all()
        for user in users:
            if int(userid)==user.sl and userpass== user.password:
                session['user2'] = userid
                details=Employee.query.filter_by(status='active').all()
                tasks=Task.query.filter_by(task_id=int(userid),taskstatus=None).all()
    
            return render_template("dashboard.html",details=details, tasks=tasks, userid=userid)
    return render_template("emplogin.html")
    

@app.route("/markComplet/<int:sl>",  methods=["GET","POST"])
def markComplete(sl):
    if request.method=="POST":
        rows=Task.query.filter_by(task_id=sl,taskstatus=None).all()
        for row in rows:
            serial=row.sl
            checklist=request.form.getlist('check')
            tasklenth=Task.query.filter_by(sl=serial, task_id=sl).all()
            for i in range (len(checklist)):
                if checklist[i]=='on':
                    print(row,sl)
                    tasklenth[i].taskstatus="complete"
                    tasklenth[i].competiondate=date.today()
                    tasklenth[i].completiontime=datetime.strftime(datetime.now(),"%H:%M:%S")

                    db.session.commit()
                else:
                    pass
            return redirect("/emp")
    return redirect("/emp")
    
@app.route("/attendance",  methods=["GET","POST"])
def attendance():
    if 'user2' in session:
        datas=db.session.query(Employee , Task).join(Task).filter(Employee.status=='active', Task.task_id==int(session['user2']), Task.taskstatus!=None )

        return render_template("/empindex.html", details=datas, userid=int(session['user2']))
    return redirect("/emp")
    
    
@app.route("/emplogout")
def emplogout():
    session.pop('user2')
    return redirect('/emp') 


app.run(debug=True)




'''
Create a program to manage a park, this program should allow the user to add staff who are responsible for maintenance, using this program, the administrator should be able to create a routine for each staff member. Each staff member should be able to mark his attendance and time spent based on the routine. There should be a provision to deactivate the staff. if a staff is deactivated, he should not be able to log in.
1. Admin--- user Id, password.
2. The employee added by Admin
3. Admin will set routine for an employee for example
                  a- employee name, Date- (autofill)
                  b- 10 to 12 work like grass cutting, 12 to 2- watering, 2 to 4- washroom cleaning.
4. Employee login page with user id and password.
Rina prasad10:38
5. Now employees are able to mark their attendance under the column of the timesheet.
6. There should be one page to create  the active or deactivate employee list for the admin and only active employees will get tasks from the admin.
7. Only Active employees can login and check their task.
 
          On Admin dashboard some points you have to mention=
Add staff
staff list
Active employee List
Routine
Attendence


'''
# @app.route("/markAttendance/<int:sl>",  methods=["GET","POST"])
# def markAttendance(sl):
#     if 'user2' in session:
#         if request.method=="POST":
#            attends=Employee.query.filter_by(status='active',sl=int(sl)).all()
           
#            if request.form.get('check')=='on':
#             # tasklenth=Attendance.query.filter_by(task_id=sl).all()
#             atten_id=sl
#             for attend in attends:
#                 name=attend.name
#             attenstatus="p"
#             attendate=datetime.now()
#             entry=Attendance(atten_id=atten_id, name=name, attendate=attendate, attenstatus=attenstatus)
#             db.session.add(entry)
#             db.session.commit()
#             return "Attendance Marked"
#     return redirect("/emp")      
"""
query="select * from table_name where lenght(name)=2"
"""
