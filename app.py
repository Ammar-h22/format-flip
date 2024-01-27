import cv2
from flask import Flask, flash, request, render_template
from werkzeug.utils import secure_filename
import os

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'webp', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.secret_key = 'super secret key'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def processImage(filename, operation):
    print(f'Filename is {filename} and operation is {operation}')
    img = cv2.imread(f'uploads/{filename}')
    match operation:
        case 'cgray':
            imgProcessed = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            newFilename = f'static/{filename}'
            cv2.imwrite(newFilename, imgProcessed)
            return newFilename
        case 'cwebp':
            newFilename = f"static/{filename.split('.')[0]}.webp"
            cv2.imwrite(newFilename, img)
            return newFilename
        case 'cpng':
            newFilename = f"static/{filename.split('.')[0]}.png"
            cv2.imwrite(newFilename, img)
            return newFilename
        case 'cjpg':
            newFilename = f"static/{filename.split('.')[0]}.jpg"
            cv2.imwrite(newFilename, img)
            return newFilename


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/edit", methods=['GET', 'POST'])
def edit():
    if request.method == 'POST':
        operation = request.form.get('operation')
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return 'Error'
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return 'No file is selected'
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            new = processImage(filename, operation)
            flash(f'Your Image has been processed! It is available <a href="/{new}" target="_blank">here</a>')
            return render_template('index.html')
    return render_template('index.html')

# app.run(debug=True)
