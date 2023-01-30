from flask import Flask, render_template, request
#from backend.controller.login import check_login
#from backend.controller.login import do_login
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from backend.klassen.User import NewUser
from backend.controller.login import do_login
import os



 #pfad noch anpassen bevors aufn server geht
template_dir = os.getcwd()
template_dir = os.path.join(template_dir, 'KlunkerkranichWebsite/frontend/templates')
app = Flask(__name__, template_folder=template_dir)
#app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:admin@localhost/mydb"
#db = SQLAlchemy()
#db.init_app(app)


#class User(db.Model):
#    id = db.Column(db.Integer, primary_key=True)
#    email = db.Column(db.String)
#    password = db.Column(db.String)



@app.route("/")
def index():
    #users = User.query.all()
    #print(users[0].email)
    return render_template('/index.html')




@app.route("/login", methods=['GET',' POST'])
def login():
    user = NewUser(request.form.get('email'),request.form.get('password'))
    loginUser = NewUser(user)
    login_response = do_login(loginUser)
    print(login_response)
    if login_response:
        return render_template('/index.html')
    else:
        return render_template('/login.html')









if __name__ == '__main__':
    app.run(port=5000, debug=True)