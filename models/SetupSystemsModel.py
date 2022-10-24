from database.db import get_connection
from .entities.SetupSystems import SetupSystems

class SetupSystemsModel():

    @classmethod
    def get_SetupSystems(self):
        try:
            connection = get_connection()
            Setupsystems = []

            with connection.cursor() as cursor:
                textSQL = """
                    SELECT idsetupsystems as id, setupsystems, rangemax, rangemin, lenguage, importance_level
                    FROM setupsystems;
                """
                cursor.execute(textSQL)
                resultset = cursor.fetchall()

                for row in resultset:
                    setupsystems = SetupSystems(row[0], row[1], row[2], row[3], row[4], row[5])
                    Setupsystems.append(setupsystems.to_JSON())

            connection.close()
            return Setupsystems
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_SetupSystem(self, id):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                textSQL = f"""
                    SELECT idsetupsystems, setupsystems, rangemax, rangemin, lenguage, importance_level
                    FROM setupsystems
                    WHERE idsetupsystems = {id};
                """
                cursor.execute(textSQL)
                row = cursor.fetchone()
                Setupsystems = None

                if row != None:
                    Setupsystems = SetupSystems(row[0], row[1], row[2], row[3], row[4], row[5])
                    Setupsystems = Setupsystems.to_JSON()

            connection.close()
            return Setupsystems
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def add_SetupSystems(self, idsetupsystems, setupsystems, rangemax, rangemin, lenguage, importancelevel):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                textSQL = f"""
                    INSERT INTO public.setupsystems(
                    idsetupsystems, setupsystems, rangemax, rangemin, lenguage, importance_level)
                    VALUES ({idsetupsystems}, '{setupsystems}', {rangemax}, {rangemin}, '{lenguage}', '{importancelevel}');
                """
                cursor.execute(textSQL)
                affected_rows = cursor.rowcount
                connection.commit()
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def update_SetupSystems(self, idsetupsystems, setupsystems, rangemax, rangemin, lenguage, importancelevel):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                textSQL = f"""
                    UPDATE public.setupsystems
                    SET  setupsystems='{setupsystems}', rangemax={rangemax}, rangemin={rangemin}, lenguage='{lenguage}', importance_level='{importance_level}'
                    WHERE idsetupsystems = {idsetupsystems};
                """
                cursor.execute(textSQL)
                affected_rows = cursor.rowcount
                connection.commit()
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)   