from src.classes_project.conexion import Conexion
from src.classes_project.manejador_excepciones import Excepciones

class Consultas:
    def __init__(self) -> None:
        pass

    def crearTablas(self):
        pass

    def insertar(self):
        pass

    def consultar(self, tabla): 
        con = Conexion()
        if con.conexion:
            try:
                sql = f"""SELECT * from {tabla}"""
                cursor = con.conexion.cursor()
                cursor.execute(sql)
                result = cursor.fetchall()

                return result
            
            except Exception as ex:
                print(
                    f"Error: requiere de su interes en consultar para la tabla {tabla}. 
                    {Excepciones().mostrarError(ex)}"
                )
                return False
            
            finally:
                #cerramos la conexión
                con.conexion.close()

        return None


    def consultarPorID():
        pass

    def modificar(self):
        pass

    def eliminar(self):
        pass