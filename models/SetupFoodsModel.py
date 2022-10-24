from database.db import get_connection
from .entities.SetupFoods import SetupFoods

class SetupFoodsModel():
    
    @classmethod
    def get_SetupFoods(self):
        try:
            connection = get_connection()
            setupfindings = []

            with connection.cursor() as cursor:
                textSQL = """
                    select idsetupfoods, s.idsetupsystems, s.setupsystems, foods, notfoods, 
                        setupfoods.rangemax, setupfoods.rangemin, setupfoods.lenguage
                    from setupfoods
                    inner join setupsystems s on s.idsetupsystems = setupfoods.idsetupsystems;
                """
                cursor.execute(textSQL)
                resultset = cursor.fetchall()

                for row in resultset:
                    setupfindingsx = SetupFoods(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
                    setupfindings.append(setupfindingsx.to_JSON())

            connection.close()
            return setupfindings

        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def get_SetupFood(self, id):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                textSQL = f"""
                    select idsetupfoods, s.idsetupsystems, s.setupsystems, foods, notfoods, 
                        setupfoods.rangemax, setupfoods.rangemin, setupfoods.lenguage
                    from setupfoods
                    inner join setupsystems s on s.idsetupsystems = setupfoods.idsetupsystems
                    WHERE idsetupfoods = {id};
                """
                cursor.execute(textSQL)
                row = cursor.fetchone()
                setupfindings = None

                if row != None:
                    setupfindings = SetupFoods(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
                    setupfindings = setupfindings.to_JSON()

            connection.close()
            return setupfindings

        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def add_SetupFood(self, IDSetupFoods, idsetupsystems, Foods, NotFoods, RangeMax, RangeMin, Lenguage):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                textSQL = f"""
                    INSERT INTO setupfoods(
                    idsetupfoods, idsetupsystems, foods, notfoods, rangemax, rangemin, lenguage)
                    VALUES ({IDSetupFoods}, {idsetupsystems}, '{Foods}', '{NotFoods}', {RangeMax}, {RangeMin}, '{Lenguage}');
                """
                cursor.execute(textSQL)
                affected_rows = cursor.rowcount
                connection.commit()
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def update_SetupFood(self, IDSetupFoods, Foods, NotFoods, RangeMax, RangeMin, Lenguage):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                textSQL = f"""
                    UPDATE public.setupfoods
                    SET foods='{Foods}', notfoods='{NotFoods}', rangemax={RangeMax}, rangemin={RangeMin}, lenguage='{Lenguage}'
                    WHERE idsetupfoods = {IDSetupFoods};
                """
                cursor.execute(textSQL)
                affected_rows = cursor.rowcount
                connection.commit()
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)