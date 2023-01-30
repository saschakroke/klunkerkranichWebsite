from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy

class Orm_user(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String)
    password = db.Column(db.String)


class Orm_employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String)
    password = db.Column(db.String)