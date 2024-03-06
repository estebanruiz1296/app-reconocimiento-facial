import bcrypt

class CifrarPassword:
    """
    Clase para cifrar contraseñas utilizando bcrypt.
    """

    @staticmethod
    def cifrar_password(password:str):
        # documentación método statico cifrar_password
        """
        Cifra una contraseña utilizando bcrypt.

        Args -
        - password (str): La contraseña en texto plano a cifrar.

        Returns:
        - str: La contraseña cifrada.
        """
        return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    
    @staticmethod
    def validar_password(password:str, hash_password:str):
        """
        Valida una contraseña cifrada con la contraseña proporcionada.

        Args:
        - password (str): La contraseña en texto plano a validar.
        - hash_password (str): La contraseña cifrada almacenada en la base de datos.

        Returns:
        - bool: True si la contraseña es válida, False en caso contrario.
        """
        return bcrypt.checkpw(password.encode(), hash_password.encode())