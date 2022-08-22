from database.db import get_connection
from .entities.AnalysisPatient import AnalysisPatient


class AnalysisPatientModel():
    
    @classmethod
    def get_AnalysisPatients(self):
        try:
            connection = get_connection()
            AnalysisPatientX = []

            with connection.cursor() as cursor:
                textSQL = """
                    SELECT idpatient, iduser, patientname, patientlastname, lenguage, birthdate, gender, weight
                    FROM analysispatient;
                """
                cursor.execute(textSQL)
                resultset = cursor.fetchall()

                for row in resultset:
                    AnalysisPatientz = AnalysisPatient(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
                    AnalysisPatientX.append(AnalysisPatientz.to_JSON())

            connection.close()
            return AnalysisPatientX
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_AnalysisPatient(self, id):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                textSQL = f"""
                    SELECT idpatient, iduser, patientname, patientlastname, lenguage, birthdate, gender, weight
                    FROM analysispatient
                    where idpatient = {id};
                """
                cursor.execute(textSQL)
                row = cursor.fetchone()

                analysispatient = None
                if row != None:
                    x = AnalysisPatient(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
                    analysispatient = x.to_JSON()

            connection.close()
            return analysispatient
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def add_AnalysisPatient(self,IDPatient, IDUser, PatientName, PatientLastName, Lenguage, BirthDate, Gender, Weight):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                textSQL = f"""
                    INSERT INTO public.analysispatient(
                        idpatient, iduser, patientname, patientlastname, 
                        lenguage, birthdate, gender, weight)
                    VALUES ({IDPatient}, {IDUser}, '{PatientName}', '{PatientLastName}', 
                    '{Lenguage}', '{BirthDate}', '{Gender}', {Weight});
                """
                cursor.execute(textSQL)
                affected_rows = cursor.rowcount
                connection.commit()
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def update_AnalysisPatient(self,IDPatient, PatientName, PatientLastName, Lenguage, BirthDate, Gender, Weight):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                textSQL = f"""
                    UPDATE public.analysispatient
                    SET patientname= '{PatientName}', patientlastname='{PatientLastName}', lenguage='{Lenguage}', 
                        birthdate='{BirthDate}', gender='{Gender}', weight={Weight}
                    WHERE idpatient = {IDPatient};
                """
                cursor.execute(textSQL)
                affected_rows = cursor.rowcount
                connection.commit()
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)