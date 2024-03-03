import pymysql
from decouple import config 

class Conexion:
    def __init__(self):
        try:
            self.connection = pymysql.connect(
                host=config('MYSQL_HOST'),
                user=config('MYSQL_USER'),
                password=config('MYSQL_PASSWORD'),
                db=config('MYSQL_DB'),
                cursorclass=pymysql.cursors.DictCursor
            )
            self.cursor = self.connection.cursor()

        except pymysql.err.OperationalError as ex:
            print('A ocurrido la siguiente excepción', ex)
            print(str(ex).split(','))
        else:
            print('¡Conexión establecida correctamente!')