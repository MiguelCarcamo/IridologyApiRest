from database.db import get_connection
from .entities.Analysis import Analysis

class AnalysisModel():
    
    @classmethod
    def get_Analysis(self):
        try:
            connection = get_connection()
            AnalysisX = []

            with connection.cursor() as cursor:
                textSQL = """
                    SELECT idanalysis, analysispatient.idpatient, analysispatient.Patientname || ' ' || analysispatient.PatientLastName as name,
                        analysispatient.iduser, iddoctor, gender,
                        case when status = 1 then 'NEW' when status = 2 then 'IN PROCESS' when status = 3 then 'COMPLETE' ELSE 'DELETE' END,
                        urlleft, urlright, createdate, finishdate
                    FROM analysis
                    LEFT JOIN analysispatient on analysis.idpatient = analysispatient.idpatient;
                """
                cursor.execute(textSQL)
                resultset = cursor.fetchall()

                for row in resultset:
                    Analysisz = Analysis(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10])
                    AnalysisX.append(Analysisz.to_JSON())

            connection.close()
            return AnalysisX
        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def get_Analysi(self, id):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                textSQL = f"""
                    SELECT idanalysis, analysispatient.idpatient, analysispatient.Patientname || ' ' || analysispatient.PatientLastName, analysispatient.iduser, iddoctor, case when status = 1 then 'NEW' when status = 2 then 'IN PROCESS' when status = 3 then 'COMPLETE' ELSE 'DELETE' END, urlleft, urlright, createdate, finishdate
                    FROM analysis
                    LEFT JOIN analysispatient on analysis.idpatient = analysispatient.idpatient
                    where idanalysis = {id};
                """
                cursor.execute(textSQL)
                row = cursor.fetchone()

                analysis = None
                if row != None:
                    x = Analysis(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9])
                    analysis = x.to_JSON()

            connection.close()
            return analysis
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def add_Analysis(self, IDAnalysis, IDPatient, URLLeft, URLRight, Status):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                textSQL = f"""
                    INSERT INTO analysis(
                    idanalysis, idpatient, createdate, status, urlleft, urlright)
                    VALUES ({IDAnalysis}, {IDPatient}, NOW(), {Status}, '{URLLeft}', '{URLRight}');
                """
                cursor.execute(textSQL)
                affected_rows = cursor.rowcount
                connection.commit()
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def update_Analysis(self, IDAnalysis, Status):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                textSQL = f"""
                    UPDATE public.analysis
                        SET status= {Status}
                    WHERE idanalysis={IDAnalysis};
                """
                cursor.execute(textSQL)
                affected_rows = cursor.rowcount
                connection.commit()
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def assigned_Analysis(self, IDAnalysis, IDDoctor, Gender):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                if Gender == 'M':
                    cursor.callproc('analisysmen',[IDAnalysis,IDDoctor])
                else:
                    cursor.callproc('analisyswomman',[IDAnalysis,IDDoctor])
                connection.commit()
                affected_rows = cursor.rowcount
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)