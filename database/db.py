import psycopg2
from psycopg2 import DatabaseError

def get_connection():
    try:
        return psycopg2.connect(
            host='208.109.191.54',
            user='postgres',
            password='Idialogi123',
            database='iridology'
        )
    except DatabaseError as ex:
        raise ex