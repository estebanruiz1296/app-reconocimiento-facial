from src.classes_project import conexion
from src.classes_project.consultas import Consultas
from datetime import date
from datetime import datetime
import bcrypt


if __name__ == '__main__':
    print('iniciando...')
    consulta = Consultas()
    #para encriptar strings

    pass_encode = "@reconocimientofacial".encode()
    sal = bcrypt.gensalt()
    pass_hasheada = bcrypt.hashpw(pass_encode, sal)

    print('insertando datos...')
    datos = {
        "identificacion" : "1084228683",
        "nombre_usuario" : "Esteban Ruiz",
        "email" : "estebanruiz1296@gmail.com",
        "password" : "@reconocimientofacial",
        "password_hash" : pass_hasheada.decode(),
        "ruta_imagen" : "d:/carpeta/predito_1299193.png",
        "fecha_registro" : str(datetime.now())
    }
    consulta.insertar('usuario', datos)

    print('consulta')
    results = consulta.consultar('usuario')
    print(results)
    



    
        
        
