""" CrearUsuario class module.
"""

from dms2021client.data.rest import AuthService

class CrearUsuario():
    """ Clase responsable mandar la orden de crear un usuario
    """

    __session_id: str
    __username: str
    __auth_service: AuthService

    def __init__(self, session_id: str, username: str, auth_service: AuthService):
        """ Initialization/constructor method.
        """

        self.__session_id = session_id
        self.__username = username
        self.__auth_service = auth_service

    def creacionUsuario(self, username, password):
        """ Método que manda la accion para la creación de un usuario.
        ---
        Parameters:
            - username: nombre de usuario a crear
            - password: contrasena de dicho usuario
        Returns:
            True si el usuario se crea con exito, False si no
        """

        status = self.__auth_service.newUser(self.__username, username, password, self.__session_id)

        if status == 200:
            salida = True
        else:
            salida = False

        return salida
