from flask import Flask, render_template, request
from backend.klassen.User import NewUser
from backend.controller.login import checkLogin
import os
#pfad noch anpassen bevors aufn server geht
template_dir = os.getcwd()
template_dir = os.path.join(template_dir, 'frontend')
template_dir = os.path.join(template_dir, 'templates')
app = Flask(__name__, template_folder=template_dir)
@app.route("/")
def index():
    return render_template('/index.html')
@app.route("/login")
def login():
    return render_template('/login.html')

@app.route("/welcome", methods=['POST'])
def welcome():
    email = request.form.get("email")
    password = request.form.get("password")
    user = NewUser(email, password)
    response = checkLogin(user)
    if response:
        return render_template('/success.html', email=email)
    else:
        return render_template('/error.html', email=email)


if __name__ == '__main__':
    app.run(port=5000, debug=True)