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
    sal = bcrypt.gensalt(15)
    pass_hasheada = bcrypt.hashpw(pass_encode, sal)

    # print('insertando datos...')
    # datos = {
    #     "identificacion" : "123456789",
    #     "nombre_usuario" : "Stiven Morales Maguaya",
    #     "email" : "morales134@gmail.com",
    #     "password" : "134morales",
    #     "password_hash" : pass_hasheada.decode(),
    #     "ruta_imagen" : "d:/carpeta/stiven_123456789.png",
    #     "fecha_registro" : str(datetime.now())
    # }
    # consulta.insertar('usuario', datos)

    # print('consulta')
    # results = consulta.consultar('usuario')
    # print(results)

    usuario_por_id = consulta.consultarPorID('usuario', '1084228683')
    print(usuario_por_id)

    print('programa finalizado.')
    



    
        
        
