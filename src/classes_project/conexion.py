import pymysql
from decouple import config 
from src.classes_project.manejador_excepciones import Excepciones

class Conexion:
    def __init__(self):
        self.conexion = None
        self.cursor = None
        try:
            self.conexion = pymysql.connect(
                host=config('MYSQL_HOST'),
                user=config('MYSQL_USER'),
                password=config('MYSQL_PASSWORD'),
                db=config('MYSQL_DB'),
                cursorclass=pymysql.cursors.DictCursor
            )
            self.cursor = self.conexion.cursor()

        except pymysql.err.OperationalError as ex:
            print('A ocurrido la siguiente excepción en Conexion: ', Excepciones().mostrarError(ex))
        else:
            print('¡Conexión establecida correctamente!')

            
            
        