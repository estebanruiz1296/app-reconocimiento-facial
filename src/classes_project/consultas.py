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
        sql = ""
        if con.conexion:
            try:
                sql = f"SHOW TABLES LIKE '{tabla}'"
                cursor = con.conexion.cursor()
                cursor.execute(sql)
                result = cursor.fetchone()
                print('existe tabla: ', result)
                if not result:
                    print('creando tabla...')
                    sql = f'''
                        CREATE TABLE `usuario` (
                            `idusuario` INT NOT NULL AUTO_INCREMENT,
                            `nombre_usuario` VARCHAR(50) NOT NULL,
                            `email` VARCHAR(50) NOT NULL,
                            `password` VARCHAR(20) NOT NULL,
                            `ruta_imagen` LONGTEXT NOT NULL,
                            `fecha_registro` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
                            PRIMARY KEY (`idusuario`)
                        )
                        ENGINE = InnoDB
                        DEFAULT CHARACTER SET = utf8
                        COLLATE = utf8_unicode_ci;
                    '''
                    cursor.execute(sql)
                    print(f'tabla {tabla} creada correctamente')

                else:
                    print('consultando...')
                    sql = f"""SELECT * from {tabla}"""
                    cursor.execute(sql)
                    result = cursor.fetchall()

                return result
            
            except Exception as ex:
                print(
                f'''
                    Error: requiere de su interes en def consultar para la tabla {tabla}. 
                    {Excepciones().mostrarError(ex)}'''
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