from database.db import get_connection
from .entities.AnalysisBodyOrgans import AnalysisBodyOrgans

class AnalysisBodyOrgansModel():
    
    @classmethod
    def get_AnalysisBodyOrgansModel(self, id):
        try:
            connection = get_connection()
            AnalysisX = []

            with connection.cursor() as cursor:
                textSQL = f"""
                    select id, idanalysis, systems, bodyorgans, bodyorgansvalue, 
                            findings, symptoms, comments , "Left" , "Right" 
                    from analysis_bodyorgans
                    where idanalysis = {id};
                """
                cursor.execute(textSQL)
                resultset = cursor.fetchall()

                for row in resultset:
                    Analysisz = AnalysisBodyOrgans(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9])
                    AnalysisX.append(Analysisz.to_JSON())

            connection.close()
            return AnalysisX
        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def update_AnalysisBodyOrgansModel(self, id, bodyorgansvalue, systems, bodyorgans):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.callproc('analisysupdate',[systems, bodyorgans, bodyorgansvalue, id])
                affected_rows = cursor.rowcount
                connection.commit()
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)