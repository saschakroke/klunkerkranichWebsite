from flask_login import login_user, LoginManager, login_required, logout_user, current_user
from flask_bcrypt import Bcrypt
from sqlalchemy.orm import relationship
from sqlalchemy.orm import declarative_base
from backend.database.querys import Querys

def check_login(user):   
    query = Querys()   
    #users = query.getAllUsers()       
    
    #return users

    return ""


