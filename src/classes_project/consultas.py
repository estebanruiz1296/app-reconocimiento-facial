from src.classes_project.conexion import Conexion
from src.classes_project.manejador_excepciones import Excepciones

class Consultas:
    def __init__(self) -> None:
        pass

    def insertar(self, tabla, datos_usuario:dict):
        con = Conexion()
        try:
            sql = f'''
                INSERT INTO {tabla} (idusuario, identificacion, nombre_usuario, email, password, password_hash, ruta_imagen, fecha_registro) 
                    VALUES 
                (
                NULL,
                '{datos_usuario['identificacion']}',
                '{datos_usuario['nombre_usuario']}', 
                '{datos_usuario['email']}',
                '{datos_usuario['password']}', 
                '{datos_usuario['password_hash']}',
                '{datos_usuario['ruta_imagen']}', 
                '{datos_usuario['fecha_registro']}')
            '''
            cursor = con.conexion.cursor()
            cursor.execute(sql)
            print('Datos registrados correctamente!')
            con.conexion.commit()

        except Exception as ex:
            print(
                f'''
                    Error: requiere de su interes en def insertar para la tabla {tabla}. 
                    {Excepciones().mostrarError(ex)}'''
                )
        finally:
            con.conexion.close()

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
                        CREATE TABLE `{tabla}` (
                            `idusuario` INT NOT NULL AUTO_INCREMENT,
                            `identificacion` VARCHAR(12) NOT NULL,
                            `nombre_usuario` VARCHAR(50) NOT NULL,
                            `email` VARCHAR(50) NOT NULL,
                            `password` VARCHAR(20) NOT NULL,
                            `password_hash` VARCHAR(100) NOT NULL,
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


    def consultarPorID(self, tabla, id):
        pass

    def modificar(self):
        pass

    def eliminar(self):
        pass