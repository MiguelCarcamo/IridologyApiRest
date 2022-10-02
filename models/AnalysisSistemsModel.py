from database.db import get_connection
from .entities.AnalysisSistems import AnalysisSistems

class AnalysisSistemsModel():
    
    @classmethod
    def get_AnalysisSistems(self, id):
        try:
            connection = get_connection()
            AnalysisX = []

            with connection.cursor() as cursor:
                textSQL = f"""
                    select id, idanalysis, systems, systemsvalue, comments 
                    from analysis_systems
                    where idanalysis = {id};
                """
                cursor.execute(textSQL)
                resultset = cursor.fetchall()

                for row in resultset:
                    Analysisz = AnalysisSistems(row[0], row[1], row[2], row[3], row[4])
                    AnalysisX.append(Analysisz.to_JSON())

            connection.close()
            return AnalysisX
        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def update_AnalysisSistems(self, id, systemsvalue, comments):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                textSQL = f"""
                    update analysis_systems
                    set systemsvalue = {systemsvalue}, comments = '{comments}'
                    where id = {id};
                """
                cursor.execute(textSQL)
                affected_rows = cursor.rowcount
                connection.commit()
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)