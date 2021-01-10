from getpass import getpass
from dms2021client.data.rest import AuthService

class CrearUsuario():

    __session_id: str
    __username: str
    __auth_service: AuthService

    def __init__(self, session_id: str, username: str, auth_service: AuthService):
        self.__session_id = session_id
        self.__username = username
        self.__auth_service = auth_service

    def creacionUsuario(self):
        """ Método que pide por paramatró nombre y contraseña para la creación de un usuario."""

        print("\n_________________________________________________\n")
        print("\nNEW USER -->")
        username: str = input('\tUsername: ')
        password: str = getpass('\tPassword: ')
        self.__auth_service.newUser(self.__username, username, password, self.__session_id)
        