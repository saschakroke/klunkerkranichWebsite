from flask_sqlalchemy import SQLAlchemy
from flask_login import login_user, LoginManager, login_required, logout_user, current_user
from flask_bcrypt import Bcrypt
from backend.klassen.User import NewUser





def checkLogin(loginUser, app):
   
    testUserDb = NewUser("ben@kro.de","1123")
    
    
    if loginUser.email == testUserDb.email and loginUser.password == testUserDb.password:
       
            login_manager = LoginManager()
            login_manager(app)
            login_user(loginUser)
            print("is drin")
            return True
          
    else:
        print("is nicht drin")
        return False



