from src.classes_project import conexion
from src.classes_project.consultas import Consultas
from datetime import date
from datetime import datetime

if __name__ == '__main__':
    print('iniciando...')
    consulta = Consultas()
    # print('insertando datos...')
    # datos = {
    #     "nombre_usuario" : "Pedrito flores",
    #     "email" : "pedrito@gmail.com",
    #     "password" : "123456",
    #     "ruta_imagen" : "d:/carpeta/predito_1299193.png",
    #     "fecha_registro" : datetime.now()
    # }
    # print(datos["email"])
    # consulta.insertar('usuario', datos)

    print('consulta')
    results = consulta.consultar('usuario')
    print(results)
    



    
        
        
