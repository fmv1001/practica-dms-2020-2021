""" LogOut class module.
"""

from dms2021client.data.rest import AuthService

class Exit():
    """ Clase responsable de hacer el logOut de un usuario
    """

    __session_id: str
    __auth_service: AuthService

    def __init__(self, session_id: str, auth_service: AuthService):
        self.__session_id = session_id
        self.__auth_service = auth_service

    def exitPagina(self):
        """ Método que permite hacer log out al usuario.
        ---
        Throws:
            Exception
        """
        try:
            self.__auth_service.logout(self.__session_id)
            return True
        except Exception as ex:
            raise ex
