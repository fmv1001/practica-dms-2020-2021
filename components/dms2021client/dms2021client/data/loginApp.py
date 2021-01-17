""" LoginApp class module.
"""

class LoginApp():
    """ Clase responsable de hacer el login de un usuario
    """

    def __init__(self, auth_service, username, password):
        """ Initialization/constructor method.
        """

        self.__auth_service = auth_service
        self.__username = username
        self.__password = password
        return

    def login(self):
        """ Método que permite loguearse al usuario.
        ---
        Returns:
            Id de la sesion que se crea
        """

        session_id: str = self.__auth_service.login(self.__username, self.__password)

        return session_id
