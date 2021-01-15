from getpass import getpass
from dms2021client.data.rest import AuthService
from dms2021client.data import crearUsuario

class CrearUsuarioPresentacion():

    __session_id: str
    __username: str
    __auth_service: AuthService

    def __init__(self, session_id: str, username: str, auth_service: AuthService):
        self.__session_id = session_id
        self.__username = username
        self.__auth_service = auth_service

    def creacionUsuario(self):
        """ Método que pide por paramatró nombre y contraseña para la creación de un usuario."""

        print("\t\n_________________________________________________\n")
        print("\t\nNEW USER -->")
        username: str = input('\t\tUsername: ')
        password: str = getpass('\t\tPassword: ')
        respuesta = crearUsuario.CrearUsuario(self.__session_id, self.__username, self.__auth_service).creacionUsuario(username, password)
        if respuesta == True:
            print("\t\t\x1b[1;32m" + "¡¡¡El usuario se ha creado con exito!!!" + "\033[0;m")
        else:
            print("\t\tError")
        
        return 0