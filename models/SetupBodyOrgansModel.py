from database.db import get_connection
from .entities.SetupBodyOrgans import SetupBodyOrgans

class SetupBodyOrgansModel():

    @classmethod
    def get_SetupBodyOrgans(self):
        try:
            connection = get_connection()
            setupbodyorgans = []

            with connection.cursor() as cursor:
                textSQL = """
                    SELECT idsetupbodyorgans, idsetupsystems, bodyorgans, "Left", "Right", 
                        men, womman, rangemax, rangemin, lenguage
	                FROM setupbodyorgans;
                """
                cursor.execute(textSQL)
                resultset = cursor.fetchall()

                for row in resultset:
                    setupbodyorgansx = SetupBodyOrgans(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9])
                    setupbodyorgans.append(setupbodyorgansx.to_JSON())

            connection.close()
            return setupbodyorgans

        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def get_SetupBodyOrgan(self, id):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                textSQL = f"""
                    SELECT idsetupbodyorgans, idsetupsystems, bodyorgans, "Left", "Right", 
                        men, womman, rangemax, rangemin, lenguage
	                FROM setupbodyorgans
                    WHERE idsetupbodyorgans = {id};
                """
                cursor.execute(textSQL)
                row = cursor.fetchone()
                setupbodyorgans = None

                if row != None:
                    setupbodyorgansx = SetupBodyOrgans(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9])
                    setupbodyorgans = setupbodyorgansx.to_JSON()

            connection.close()
            return setupbodyorgans

        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def add_SetupBodyOrgan(self, IDSetupBodyOrgans, IDSetupSystems, BodyOrgans, Left, Right, Men, Womman, RangeMax, RangeMin, Lenguage):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                textSQL = f"""
                    INSERT INTO setupbodyorgans(
                        idsetupbodyorgans, idsetupsystems, bodyorgans, "Left", "Right", 
                        men, womman, rangemax, rangemin, lenguage)
                        VALUES ({IDSetupBodyOrgans}, {IDSetupSystems}, '{BodyOrgans}', CAST({Left} AS bit), CAST({Right} AS bit), 
                                CAST({Men} AS bit), CAST({Womman} AS bit), {RangeMax}, {RangeMin}, '{Lenguage}');
                """
                cursor.execute(textSQL)
                affected_rows = cursor.rowcount
                connection.commit()
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def update_SetupBodyOrgan(self, IDSetupBodyOrgans, IDSetupSystems, BodyOrgans, Left, Right, Men, Womman, RangeMax, RangeMin, Lenguage):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                textSQL = f"""
                    UPDATE setupbodyorgans
                    SET  idsetupsystems={IDSetupSystems}, bodyorgans='{BodyOrgans}', "Left"=CAST({Left} AS bit), "Right"=CAST({Right} AS bit), 
                        men=CAST({Men} AS bit), womman=CAST({Womman} AS bit), rangemax={RangeMax}, rangemin={RangeMin}, lenguage='{Lenguage}'
                    WHERE idsetupbodyorgans = {IDSetupBodyOrgans};
                """
                cursor.execute(textSQL)
                affected_rows = cursor.rowcount
                connection.commit()
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)