import psycopg2
from psycopg2 import DatabaseError

def get_connection():
    try:
        return psycopg2.connect(
            host='ec2-50-19-255-190.compute-1.amazonaws.com',
            user='waurhzodsccaoj',
            password='07586a7a5e0edf933eadf34d4fa15a7fef79d8f406ea1bb0c79cc1ee004f029f',
            database='dcaqg5enote566'
        )
    except DatabaseError as ex:
        raise ex