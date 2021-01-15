from dms2021client.data.rest import AuthService

class CrearUsuario():

    __session_id: str
    __username: str
    __auth_service: AuthService

    def __init__(self, session_id: str, username: str, auth_service: AuthService):
        self.__session_id = session_id
        self.__username = username
        self.__auth_service = auth_service

    def creacionUsuario(self, username, password):
        """ Método que pide por paramatró nombre y contraseña para la creación de un usuario."""

        status = self.__auth_service.newUser(self.__username, username, password, self.__session_id)
        
        if status == 200:
            salida = True
        else:
            salida = False

        return salida