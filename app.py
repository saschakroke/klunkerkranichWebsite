from flask import Flask, render_template, request
from flask_login import login_required
from backend.controller.login import checkLogin
from backend.klassen.User import NewUser


import os



 #pfad noch anpassen bevors aufn server geht
template_dir = os.getcwd()
template_dir = os.path.join(template_dir, 'KlunkerkranichWebsite/frontend/templates')
app = Flask(__name__, template_folder=template_dir)


@app.route("/")
def index():
    return render_template('/index.html')


@app.route("/login", methods=['GET',' POST'])
def login():
    email =  request.form.get('email')
    password =  request.form.get('password')

    loginUser = NewUser(email, password)
    
    login_response = checkLogin(loginUser,app)

    if login_response:
        return render_template('/index.html')
    else:
        return render_template('/login.html')











if __name__ == '__main__':
    app.run(port=5000, debug=True)