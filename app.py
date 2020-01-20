from flask import Flask, render_template, request, send_file, flash, redirect, session, abort, url_for, jsonify
import pymysql
import json
from flask_wtf.csrf import CsrfProtect
#from PayTM import Checksum
import requests
import pyrebase
from werkzeug import secure_filename
import os

UPLOAD_FOLDER = 'static/image_upload/'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER




config = {
  "apiKey": "AIzaSyCOzfbPE-zd1_bHq3ROzmszjZP5cu0yuVI",
  "authDomain": "plothole-sih.firebaseapp.com",
  "databaseURL": "https://plothole-sih.firebaseio.com",
  "storageBucket": "plothole-sih.appspot.com"
}

firebase = pyrebase.initialize_app(config)
storage = firebase.storage()


@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        if request.form['submit'] == 'Admin':
            print("Admin")
        


        if request.form['submit'] == 'User':
            print("User")


    return render_template('index.html')


@app.route('/userlogin', methods=["GET", "POST"])
def userlogin():
    if request.method == "POST":
        if request.form['submit'] == 'Login':
            #print("Admin")
            payload = {'email' : request.form.get('email'), 'password' : request.form.get('password')}
            print(payload)
            # Get a reference to the auth service
            auth = firebase.auth()

            # Log the user in
            try:
                user = auth.sign_in_with_email_and_password(payload["email"], payload["password"])
                db = firebase.database()

                # data to save
                data = {
                    "name": payload["email"],
                    "token": user["idToken"]
                }

                # Pass the user's idToken to the push method
                results = db.child("users").push(data, user['idToken'])
                print(results)
                return redirect(url_for('adminlogin'))
            except:
                pass

            # Get a reference to the database service
            




    return render_template('userLogin.html')


@app.route('/adminpanel', methods=["GET", "POST"])
def adminpanel():
    if request.method == "POST":
        if request.form['submit'] == 'Admin':
            print("Admin")
        


        if request.form['submit'] == 'User':
            print("User")


    return render_template('adminPanel.html')


@app.route('/userpanel', methods=["GET", "POST"])
def userpanel():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            #upload to firebase

            storage.child(filename).put("static/image_upload/"+filename)




            return redirect(url_for('index'))
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS



if __name__ == "__main__":
	app.run(host='0.0.0.0', port=8001, debug=True)