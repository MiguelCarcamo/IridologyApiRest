from database.db import get_connection
from .entities.User import User


class UserModel():

    @classmethod
    def get_users(self):
        try:
            connection = get_connection()
            users = []

            with connection.cursor() as cursor:
                textSQL = """
                    SELECT idinfouser, username, userlastname, usermail, userphone, usercountry, userlenguage,
                        "User", "Password", case Status when '1' then 'Active' else 'deactivated' end as Status,
                        TypeUser.TypeUser, TypeUser.IDTypeUser
                    FROM infouser
                    LEFT JOIN TypeUser ON infouser.IDTypeUser = TypeUser.IDTypeUser;
                """
                cursor.execute(textSQL)
                resultset = cursor.fetchall()

                for row in resultset:
                    user = User(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11])
                    users.append(user.to_JSON())

            connection.close()
            return users
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_user(self, id):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                textSQL = f"""
                    SELECT idinfouser, username, userlastname, usermail, userphone, usercountry, userlenguage,
                        "User", "Password", case Status when '1' then 'Active' else 'deactivated' end as Status,
                        TypeUser.TypeUser, TypeUser.IDTypeUser
                    FROM infouser
                    LEFT JOIN TypeUser ON infouser.IDTypeUser = TypeUser.IDTypeUser
                    WHERE idinfouser = {id};
                """
                cursor.execute(textSQL)
                row = cursor.fetchone()

                user = None
                if row != None:
                    user = User(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11])
                    user = user.to_JSON()

            connection.close()
            return user
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def add_user(self, idinfouser, username, userlastname, usermail, userphone, usercountry, userlenguage, user, Password, idtypeuser):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                textSQL = f"""
                    INSERT INTO public.infouser(
                    idinfouser, username, userlastname, usermail, 
                    userphone, usercountry, userlenguage, "User", 
                    "Password", status, idtypeuser)
                    VALUES ({idinfouser}, '{username}', '{userlastname}', '{usermail}',
                            '{userphone}', '{usercountry}', '{userlenguage}', '{user}',
                            '{Password}', CAST(1 AS bit), {idtypeuser});
                """
                cursor.execute(textSQL)
                affected_rows = cursor.rowcount
                connection.commit()
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def update_user(self, idinfouser, username, userlastname, usermail, userphone, usercountry, userlenguage, Password, idtypeuser, Status):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                textSQL = f"""
                    UPDATE infouser
                    SET username='{username}', userlastname='{userlastname}', usermail='{usermail}', userphone='{userphone}', usercountry='{usercountry}', userlenguage='{userlenguage}', "Password"='{Password}', idtypeuser='{idtypeuser}', Status = '{Status}'
                    WHERE idinfouser={idinfouser};
                """
                cursor.execute(textSQL)
                affected_rows = cursor.rowcount
                connection.commit()
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def login_user(self, Xuser, password):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                textSQL = f"""
                    SELECT idinfouser, username, userlastname, usermail, userphone, usercountry, userlenguage,
                        "User", "Password", Status,
                        TypeUser.TypeUser
                    FROM infouser
                    LEFT JOIN TypeUser ON infouser.IDTypeUser = TypeUser.IDTypeUser
                    WHERE "User" = '{Xuser}' AND "Password" = '{password}';
                """
                cursor.execute(textSQL)
                row = cursor.fetchone()

                user = None
                if row != None:
                    user = User(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10])
                    user = user.to_JSON()

            connection.close()
            return user
        except Exception as ex:
            raise Exception(ex)