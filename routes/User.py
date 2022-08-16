from flask import Blueprint, jsonify, request

from models.UserModel import UserModel
from database.db import get_connection

main=Blueprint('user_blueprint', __name__)

@main.route('/')
def get_users():
    try:
        users = UserModel.get_users()
        return jsonify(users)
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

@main.route('/<id>')
def get_user(id):
    try:
        user = UserModel.get_user(id)
        if user != None:
            return jsonify(user)
        else:
            return jsonify({}), 404
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

@main.route('/add', methods=['POST'])
def add_user():
    try:
        user_details = request.get_json()

        username= user_details[0]['UserName']
        userlastname= user_details[0]['UserLastName']
        usermail= user_details[0]['UserMail']
        userphone= user_details[0]['UserPhone']
        usercountry= user_details[0]['UserCountry']
        userlenguage= user_details[0]['UserLenguage']
        userPassword= user_details[0]['userPassword']
        xUser= userlastname.lower().split()[0]+username.lower().split()[0]
        connection = get_connection()
        with connection.cursor() as cursor:
            cursor.execute("SELECT coalesce(max(idinfouser),0) + 1 from infouser")
            id = cursor.fetchone()
            cursor.execute(f"""SELECT coalesce(max(idinfouser),0) + 1 from infouser WHERE "User" like '%{xUser}%'""")
            count = cursor.fetchone()
        connection.close()
        idinfouser= int(id[0])
        xUser = xUser + str(count[0])
        Status= 1
        TypeUser= user_details[0]['TypeUser']

        affected_rows = UserModel.add_user(idinfouser, username, userlastname, usermail, userphone, usercountry, userlenguage, xUser, userPassword, TypeUser )

        if affected_rows == 1:
            import smtplib, ssl
            port = 465  # For SSL
            smtp_server = "smtp.gmail.com"
            sender_email = "iridology.app@gmail.com"  # Enter your address
            receiver_email = usermail  # Enter receiver address
            password = "ccbgmkysnepjjikw"
            message = f"""\
            Subject: Welcome to App Iridology

            Your username is: {xUser}"""

            context = ssl.create_default_context()
            with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
                server.login(sender_email, password)
                server.sendmail(sender_email, receiver_email, message)
            return dict(msj='Accion Realizada Correctamente')
        else:
            return dict(msj='Accion no fue Completada'), 500

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

@main.route('/update/', methods=['PUT'])
def update_user():
    try:
        user_details = request.get_json()

        username= user_details[0]['UserName']
        userlastname= user_details[0]['UserLastName']
        usermail= user_details[0]['UserMail']
        userphone= user_details[0]['UserPhone']
        usercountry= user_details[0]['UserCountry']
        userlenguage= user_details[0]['UserLenguage']
        idinfouser = user_details[0]['idinfouser']
        TypeUser= user_details[0]['TypeUser']
        userPassword = user_details[0]['userPassword']

        affected_rows = UserModel.update_user(idinfouser, username, userlastname, usermail, userphone, usercountry, userlenguage, userPassword, TypeUser )

        if affected_rows == 1:
            return dict(msj='Accion Realizada Correctamente')
        else:
            return dict(msj='Accion no fue Completada'), 500

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

@main.route('/login/', methods=['POST'])
def login_user():
    try:
        user_details = request.get_json()

        XUser= user_details[0]['user']
        userPassword = user_details[0]['userPassword']

        user = UserModel.login_user(XUser, userPassword)

        if user != None:
            return jsonify(user)
        else:
            return dict(msj='Accion no fue Completada'), 500

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500