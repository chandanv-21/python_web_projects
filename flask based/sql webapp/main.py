from flask import Flask, render_template, request, session, redirect
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
import os
local_server = True
app=Flask(__name__)
if local_server:
    app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:admin@localhost/courier"
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:admin@localhost/courier"
app.config['SECRET_KEY'] = 'the random string'
db=SQLAlchemy(app)

class Consumerdetails(db.Model):
    sl = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=False)
    email = db.Column(db.String(80), unique=False)
    phone = db.Column(db.String(25), unique=True)
    address = db.Column(db.String(500), unique=True)
    pickupdate = db.Column(db.String(20), unique=False)
    weight = db.Column(db.String(12), unique=False)
    destination = db.Column(db.String(25), unique=False)
    price = db.Column(db.String(25), unique=False)
    photo = db.Column(db.String(25), unique=False)
    status = db.Column(db.String(25), unique=False)
    updates=db.relationship('Update',backref='consumerdetails', lazy=True)


class Update(db.Model):
    sl=db.Column(db.Integer, primary_key=True)
    update_id = db.Column(db.Integer, db.ForeignKey('consumerdetails.sl')) 
    currentstatus = db.Column(db.String(100), unique=False)
    date_time = db.Column(db.String(20), unique=False)


destinations={'delhi':500,'mumbai':650, 'chennai':800,'banglore':820,'kolkat':450,'pune':660}
@app.route("/", methods=["GET","POST"])
def index():
    if 'user' in session and session['user'] == 'chandan':
        datas=Consumerdetails.query.filter_by(status='active').all()
        return render_template("index.html",datas=datas)
    if request.method == 'POST':
        username = request.form.get('email')
        userpass = request.form.get('password')
        if (username == 'chandan') and (userpass == 'Password'):
            session['user'] = username
            datas=Consumerdetails.query.filter_by(status='active').all()
            return render_template("index.html",datas=datas)
    return render_template("login.html")


@app.route("/insert/", methods=["GET","POST"])
def insert():
    if 'user' in session and session['user'] == 'chandan':
        return render_template('insert.html')
    

@app.route("/insertdata", methods=["POST"])
def insertdata():
    if 'user' in session and session['user'] == 'chandan':
        name=request.form.get("name")
        email=request.form.get("email")
        phone=request.form.get("phone")
        address=request.form.get("address")
        pickupdate=request.form.get("pickupdate")
        weight=request.form.get("weight")
        destination=request.form.get("destination")
        destinations={'delhi':500,'mumbai':650, 'chennai':800,'banglore':820,'kolkat':450,'pune':660}
        photo=request.files["photo"]
        status='active'
        price=int(weight)*destinations[destination]

        photo.save(os.path.join('static/images',photo.filename))
        entry = Consumerdetails(name=name, email=email, phone=phone, address=address, pickupdate=pickupdate, weight=weight, destination=destination, price=price, photo=photo.filename, status=status )
        db.session.add(entry)
        db.session.commit()
        return redirect("/")
    return redirect("/")


@app.route("/manage")
def manage():
    if 'user' in session and session['user'] == 'chandan':
        datas=Consumerdetails.query.filter_by(status='active').all() 
        return render_template("manage.html",datas=datas)
    return redirect("/")


@app.route("/delete/<int:sl>")
def delete(sl):
    if 'user' in session and session['user'] == 'chandan':
        data=Consumerdetails.query.filter_by(sl=sl).first()
        data.status="deleted"
        db.session.add(data)
        db.session.commit()
        
        return redirect("/manage")
    return redirect("/")


@app.route("/edit/<int:sl>", methods=["GET","POST"])
def edit(sl):
    if 'user' in session and session['user'] == 'chandan':
        if request.method=="POST":
            name=request.form.get("name")
            email=request.form.get("email")
            phone=request.form.get("phone")
            address=request.form.get("address")
            pickupdate=request.form.get("pickupdate")
            weight=request.form.get("weight")
            destination=request.form.get("destination")
            fphoto=request.files["photo"]
            destinations={'delhi':500,'mumbai':650, 'chennai':800,'banglore':820,'kolkat':450,'pune':660}
            price=int(weight)*destinations[destination]
            
            data=Consumerdetails.query.filter_by(sl=sl).first()
            fname=data.photo
            if  fphoto.filename!="":
                print("IF loop")
                try:
                    fphoto.save(os.path.join('static/images',fphoto.filename))
                except Exception as e:
                    print("Error is ",e)
                data.name=name
                data.email=email
                data.phone=phone
                data.address=address
                data.pickupdate=pickupdate   
                data.weight=weight
                data.destination=destination
                data.price=price
                data.photo=fphoto.filename
                db.session.commit()
            else:
                print("Else loop")
                data.name=name
                data.email=email
                data.phone=phone
                data.address=address
                data.pickupdate=pickupdate   
                data.weight=weight
                data.destination=destination
                data.price=price
                db.session.commit()
            return redirect("/manage")
        data=Consumerdetails.query.filter_by(sl=sl).first()
        return render_template("edit.html", data=data,sl=sl)
    return redirect("/")    
    

@app.route("/restore")
def restore():
    if 'user' in session and session['user'] == 'chandan':
        datas=Consumerdetails.query.filter_by(status='deleted').all() 
        return render_template("recycle.html",datas=datas)
    return redirect("/")


@app.route("/recycled/<int:sl>")
def recycled(sl):
    if 'user' in session and session['user'] == 'chandan':
        data=Consumerdetails.query.filter_by(sl=sl).first()
        data.status="active"
        db.session.add(data)
        db.session.commit()
        return redirect("/restore")
    return redirect("/")


@app.route("/details/<int:sl>")
def details(sl):
    if 'user' in session and session['user'] == 'chandan':
    # datas=db.session.query(Consumerdetails, Update).join(Consumerdetails).filter(Consumerdetails.status=='active',Update.update_id==sl)
        datas=Consumerdetails.query.filter_by(sl=sl).all()
        datas2=Update.query.filter_by(update_id=sl).all()
        return render_template("details.html",datas=datas, datas2=datas2, sl=sl)
    return redirect("/")


@app.route("/updateStatus/<int:sl>", methods=['GET','POST'])
def updateStatus(sl):
    if 'user' in session and session['user'] == 'chandan':
        if request.method=='POST':
            newstatus=request.form.get('currentstatus')
            form_date=request.form.get('date')
            form_time=request.form.get('time')
            print(form_date,form_time)
            date_time=datetime.strptime(form_date + " "+ form_time +":00", "%Y-%m-%d %H:%M:%S")
            update_id=sl
            entry=Update(update_id=update_id, currentstatus=newstatus,date_time=date_time)
            db.session.add(entry)
            db.session.commit()
            updates=Update.query.filter_by(update_id=sl).all()
            return redirect(f"/updateStatus/{sl}")
        updates=Update.query.filter_by(update_id=sl).all()
        return render_template("updateStatus.html", updates=updates, sl=sl)
    return redirect("/")


@app.route("/logout")
def logout():
    session.pop('user')
    return redirect('/')


app.run(debug=True)