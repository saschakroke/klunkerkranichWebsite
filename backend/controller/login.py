from backend.klassen.User import NewUser


def checkLogin(user):
    databaseObject = NewUser("ben@kro.de", "123")

    if user.email == databaseObject.email and user.password == databaseObject.password:
        return True
    else:
        return False



