import psycopg2
from psycopg2 import DatabaseError

def get_connection():
    try:
        return psycopg2.connect(
            host='ec2-44-206-214-233.compute-1.amazonaws.com',
            user='wfldkdohudqmvn',
            password='1dd039070e834b07ce6fb4d143b0fcf71ec3fcdcb36c1105b086abd3bc194e6f',
            database='d22q19sngc4mt2'
        )
    except DatabaseError as ex:
        raise ex