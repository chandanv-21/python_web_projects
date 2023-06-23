from flask import Flask,render_template, redirect, request, flash
import cv2
from werkzeug.utils import secure_filename
import os

UPLOAD_FOLDER = "uploads"
ALLOWED_EXTENTIONS = {"jpg", "jpeg", "png", "webp"}
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SECRET_KEY'] = 'super secret key'

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENTIONS

def processImage(filename, operation):
    print(f"The operation is {operation} and filename is {filename}")
    img= cv2.imread(f"uploads/{filename}")
    match operation:
        case "cgray":
            imgProcessed = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            cv2.imwrite(f"static/{filename}", imgProcessed) 
            return filename
        case "cjpg":
            newFilename = f"static/{filename.split('.')[0]}.jpg"
            cv2.imwrite(newFilename, img) 
            return newFilename
        case "cpng":
            newFilename = f"static/{filename.split('.')[0]}.png"
            cv2.imwrite(newFilename, img) 
            return newFilename
        case "cwebp":
            newFilename = f"static/{filename.split('.')[0]}.webp"
            cv2.imwrite(newFilename, img) 
            return newFilename


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/edit", methods = ["GET", "POST"])
def edit():
    if request.method == "POST":
        if 'file' not in request.files:
            flash("No file part")
            return redirect(request.url)
        else:
            file= request.files['file']
            if file.filename == '':
                flash('No selected file')
                return "No file is selected.."
            if file and allowed_file(file.filename):
                filename= secure_filename( file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                new = processImage(filename, request.form.get('operation'))
                flash(f"Your image has been processed and is avaialable <a href='/{new}' target='_blank' >here</a>")
                return render_template("index.html")
            
            
        return "POST request is here... "


app.run(debug=True)