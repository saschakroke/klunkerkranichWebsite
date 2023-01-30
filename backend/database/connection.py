from flask_sqlalchemy import SQLAlchemy

class Connection():
    def __init__(self, app):
        db = SQLAlchemy()
        #engine = create_engine("mysql+pymysql://root:admin@localhost/kk_db")
        app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:admin@localhost/mydb"
        db.init_app(app)

    
    
    