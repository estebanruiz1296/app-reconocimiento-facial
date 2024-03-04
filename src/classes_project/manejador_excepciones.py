import re

class Excepciones:
    def __init__(self):
        self.errores:dict = {
            "2003" : "No se puede establecer una conexión con el servidor de bases de datos",
            "1049" : "La base de datos a la cual se quiere conectar no existe",
            "1146" : "La tabla consultada no existe",
        } 

    def mostrarError(self, cod):
        msg_ex = str(cod).split(',')[0]
        regex_cod = re.sub(r'\(', '', msg_ex)
        self.cod_ex = regex_cod

        for c in self.errores.keys():
            if c == regex_cod:
                return int(regex_cod), self.errores[regex_cod]
            
        return f"Código desconocido: {regex_cod}", cod