class User():

    def __init__(self, idinfouser, username=None, userlastname=None, usermail=None, userphone=None, usercountry=None, userlenguage=None, User=None, Password=None, status=None, typeuser=None, idtypeuser=None) -> None:
        self.idinfouser = idinfouser
        self.username = username
        self.userlastname = userlastname
        self.usermail = usermail
        self.userphone = userphone
        self.usercountry = usercountry
        self.userlenguage = userlenguage
        self.User = User
        self.Password = Password
        self.status = status
        self.typeuser = typeuser
        self.idtypeuser = idtypeuser

    def to_JSON(self):
        return {
            'id': self.idinfouser,
            'username': self.username,
            'userlastname': self.userlastname,
            'usermail': self.usermail,
            'userphone': self.userphone,
            'usercountry': self.usercountry,
            'userlenguage': self.userlenguage,
            'User': self.User,
            'Password': self.Password,
            'status': self.status,
            'typeuser': self.typeuser,
            'idtypeuser': self.idtypeuser,
        }