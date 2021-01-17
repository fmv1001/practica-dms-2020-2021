""" ExitPresentacion class module.
"""

import time
from dms2021client.data.rest import AuthService
from dms2021client.data.logoutApp import Exit

class ExitPresentacion():
    """ Clase responsable de la interfaz correspondiente a un logOut
    """

    __session_id: str
    __auth_service: AuthService

    def __init__(self, session_id: str, auth_service: AuthService):
        """ Initialization/constructor method.
        """

        self.__session_id = session_id
        self.__auth_service = auth_service

    def exitPagina(self):
        """ Permite al usuario hacer un LogOut. """

        try:
            Exit(self.__session_id, self.__auth_service).exitPagina()
            print("\x1b[1;31m" + "+----------------------------+")
            print("| Logged out successfully    |")
            print("+----------------------------+" + "\033[0;m")
            time.sleep(2)
            return -1
        except Exception as ex:
            print(ex)
