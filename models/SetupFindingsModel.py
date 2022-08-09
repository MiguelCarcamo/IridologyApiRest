from database.db import get_connection
from .entities.SetupFindings import SetupFindings

class SetupFindingsModel():
    
    @classmethod
    def get_SetupFindings(self):
        try:
            connection = get_connection()
            setupfindings = []

            with connection.cursor() as cursor:
                textSQL = """
                    SELECT idsetupfindings, idsetupbodyorgans, foods, notfoods, findings, 
                           rangemax, rangemin, lenguage
	                FROM setupfindings;
                """
                cursor.execute(textSQL)
                resultset = cursor.fetchall()

                for row in resultset:
                    setupfindingsx = SetupFindings(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
                    setupfindings.append(setupfindingsx.to_JSON())

            connection.close()
            return setupfindings

        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def get_SetupFinding(self, id):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                textSQL = f"""
                    SELECT idsetupfindings, idsetupbodyorgans, foods, notfoods, findings, 
                           rangemax, rangemin, lenguage
	                FROM setupfindings
                    WHERE idsetupfindings = {id};
                """
                cursor.execute(textSQL)
                row = cursor.fetchone()
                setupfindings = None

                if row != None:
                    setupfindings = SetupFindings(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
                    setupfindings = setupfindings.to_JSON()

            connection.close()
            return setupfindings

        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def add_SetupFinding(self, IDSetupFindings, IDSetupBodyOrgans, Foods, NotFoods, Findings, RangeMax, RangeMin, Lenguage):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                textSQL = f"""
                    INSERT INTO public.setupfindings(
                    idsetupfindings, idsetupbodyorgans, foods, notfoods, findings, rangemax, rangemin, lenguage)
                    VALUES ({IDSetupFindings}, {IDSetupBodyOrgans}, '{Foods}', '{NotFoods}', '{Findings}', {RangeMax}, {RangeMin}, '{Lenguage}');
                """
                cursor.execute(textSQL)
                affected_rows = cursor.rowcount
                connection.commit()
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def update_SetupFinding(self, IDSetupFindings, IDSetupBodyOrgans, Foods, NotFoods, Findings, RangeMax, RangeMin, Lenguage):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                textSQL = f"""
                    UPDATE public.setupfindings
                    SET idsetupbodyorgans={IDSetupBodyOrgans}, foods='{Foods}', notfoods='{NotFoods}', findings='{Findings}', rangemax={RangeMax}, rangemin={RangeMin}, lenguage='{Lenguage}'
                    WHERE idsetupfindings= {IDSetupFindings};
                """
                cursor.execute(textSQL)
                affected_rows = cursor.rowcount
                connection.commit()
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)