import os, random
from flask import Flask, flash, request, redirect, url_for, render_template, jsonify
from flask import send_from_directory
from werkzeug.utils import secure_filename 
import base64 

UPLOAD_FOLDER = './uploads'
ALLOWED_EXTENSIONS = set(['pdf', 'png', 'jpg', 'jpeg', 'gif'])
CURR_OPPONENT = ""
CURR_IMAGE = ""

app = Flask(__name__)
app.secret_key = "PeterIsTheBest"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET','POST'])
def index():
    return render_template('webcam_test.html')

@app.route('/_upload_file', methods=['POST'])
def upload_file():
    print(request.data)
    encoding = request.data.decode('base64')
    print(encoding)
    fh = open("imageToSave.png", "wb")
    fh.write(encoding.decode('base64'))
    fh.close()
    return jsonify({'success':True})

@app.route('/_return_pic', methods=['GET'])
def return_pic():
    #name = request.args.get(data, 0, type=int)
    #name = request.data
    if request.method == "GET":
        name = request.url
        name = name.split("\\")[-1]
        with open("uploads/" + name, "rb") as image_file:
            encoded_img = base64.b64encode(image_file.read())
        percent_score = analyze_image(CURR_IMAGE,CURR_OPPONENT)
        return jsonify(percent=percent_score,returned_pic=encoded_img)
        return false
        #return render_template('form.html')
    else:
        return "nothing"
    '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''

@app.route('/uploads/<filename>')
def uploaded_file(filename):    
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)

def analyze_image(pic1, pic2):
    #Add code to insert filename here, return score
    return '90' 

@app.route('/_reset_image', methods=['GET'])
def reset_image():
    name = random.choice(os.listdir("./uploads/"))
    CURR_OPPONENT = "uploads/" + name
    with open("uploads/" + name, "rb") as image_file:
        encoded_img = base64.b64encode(image_file.read())
    percent_score = analyze_image(CURR_OPPONENT, CURR_IMAGE)
    print(percent_score)
    return jsonify(returned_pic=encoded_img)

