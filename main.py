from src.classes_project import conexion
from src.classes_project.consultas import Consultas

if __name__ == '__main__':
    print('iniciando...')
    consulta = Consultas().consultar('usuario')
    print(consulta)
    



    
        
        
