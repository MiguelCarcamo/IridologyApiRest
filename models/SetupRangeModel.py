from database.db import get_connection
from .entities.SetupRange import SetupRange

class SetupFoodsModel():
    
    @classmethod
    def get_SetupRanges(self):
        try:
            connection = get_connection()
            setuprange = []

            with connection.cursor() as cursor:
                textSQL = """
                    select idsetuprange, setuprange, rangemin, rangemax
                    from setuprange;
                """
                cursor.execute(textSQL)
                resultset = cursor.fetchall()

                for row in resultset:
                    setuprangex = SetupRange(row[0], row[1], row[3], row[2])
                    setuprange.append(setuprangex.to_JSON())

            connection.close()
            return setuprange

        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def add_SetupRanges(self, idsetuprange, setuprange, RangeMax, RangeMin):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                textSQL = f"""
                    INSERT INTO setuprange(
                    idsetuprange, setuprange, rangemax, rangemin)
                    VALUES ({idsetuprange}, '{setuprange}', {RangeMax}, {RangeMin});
                """
                cursor.execute(textSQL)
                affected_rows = cursor.rowcount
                connection.commit()
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def update_SetupRanges(self, idsetuprange, setuprange, RangeMax, RangeMin):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                textSQL = f"""
                    UPDATE public.setuprange
                    SET setuprange='{setuprange}', rangemax={RangeMax}, rangemin={RangeMin}
                    WHERE idsetuprange = {idsetuprange};
                """
                cursor.execute(textSQL)
                affected_rows = cursor.rowcount
                connection.commit()
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)