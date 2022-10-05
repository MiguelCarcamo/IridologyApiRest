from database.db import get_connection
from .entities.SetupSymptoms import SetupSymptoms

class SetupSymptomsModel():
    
    @classmethod
    def get_SetupSymptoms(self):
        try:
            connection = get_connection()
            setupsymptoms = []

            with connection.cursor() as cursor:
                textSQL = """
                    SELECT idsetupsymptoms, setupbodyorgans.idsetupbodyorgans, setupbodyorgans.bodyorgans, symptoms, setupsymptoms.rangemax, setupsymptoms.rangemin, setupsymptoms.lenguage
                    FROM setupsymptoms
                    LEFT JOIN setupbodyorgans on setupsymptoms.idsetupbodyorgans = setupbodyorgans.idsetupbodyorgans;
                """
                cursor.execute(textSQL)
                resultset = cursor.fetchall()

                for row in resultset:
                    setupsymptomsx = SetupSymptoms(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
                    setupsymptoms.append(setupsymptomsx.to_JSON())

            connection.close()
            return setupsymptoms

        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_SetupSymptom(self, id):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                textSQL = f"""
                    SELECT idsetupsymptoms, setupbodyorgans.idsetupbodyorgans, setupbodyorgans.bodyorgans, symptoms, setupsymptoms.rangemax, setupsymptoms.rangemin, setupsymptoms.lenguage
                    FROM setupsymptoms
                    LEFT JOIN setupbodyorgans on setupsymptoms.idsetupbodyorgans = setupbodyorgans.idsetupbodyorgans;
                    WHERE idsetupsymptoms = {id};
                """
                cursor.execute(textSQL)
                row = cursor.fetchone()
                setupsymptoms = None

                if row != None:
                    setupsymptomsx = SetupSymptoms(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
                    setupsymptoms = setupsymptomsx.to_JSON()

            connection.close()
            return setupsymptoms

        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def add_SetupSymptom(self, IDSetupSymptoms, IDSetupBodyOrgans, Symptoms, RangeMax, RangeMin, Lenguage):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                textSQL = f"""
                    INSERT INTO public.setupsymptoms(
                    idsetupsymptoms, idsetupbodyorgans, symptoms, rangemax, rangemin, lenguage)
                    VALUES ({IDSetupSymptoms}, {IDSetupBodyOrgans}, '{Symptoms}', {RangeMax}, {RangeMin}, '{Lenguage}');
                """
                cursor.execute(textSQL)
                affected_rows = cursor.rowcount
                connection.commit()
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def update_SetupSymptom(self, IDSetupSymptoms, IDSetupBodyOrgans, Symptoms, RangeMax, RangeMin, Lenguage):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                textSQL = f"""
                    UPDATE public.setupsymptoms
                    SET idsetupbodyorgans={IDSetupBodyOrgans}, symptoms='{Symptoms}', rangemax={RangeMax}, rangemin={RangeMin}, lenguage='{Lenguage}'
                    WHERE idsetupsymptoms={IDSetupSymptoms};
                """
                cursor.execute(textSQL)
                affected_rows = cursor.rowcount
                connection.commit()
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)

    def delete_SetupSymptom(self, IDSetupSymptoms):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                textSQL = f"""
                    delete
                    from setupsymptoms
                    WHERE idsetupsymptoms={IDSetupSymptoms};
                """
                cursor.execute(textSQL)
                affected_rows = cursor.rowcount
                connection.commit()
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)