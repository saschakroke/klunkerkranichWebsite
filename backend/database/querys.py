from flask_sqlalchemy import SQLAlchemy
import app
db = SQLAlchemy

class Orm_user(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String)
    password = db.Column(db.String)

class Querys():
        
    def __init__(self, app):
        db = SQLAlchemy()
        #engine = create_engine("mysql+pymysql://root:admin@localhost/kk_db")
        app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:admin@localhost/mydb"
        db.init_app(app)


    def getAllUsers():
        ormUserModels = Orm_user().query.all()
        return ormUserModels


