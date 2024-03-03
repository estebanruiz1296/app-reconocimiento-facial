class Excepciones:

    def __init__(self):
        self.codigo_error = ""
        self.mensaje = ""

    def generarExcepcion(self, mysql=None, codigo:str=''):
        return codigo