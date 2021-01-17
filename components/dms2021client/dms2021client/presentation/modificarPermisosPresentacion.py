""" ModificarPermisosPresentacion class module.
"""

from dms2021client.data.rest import AuthService
from dms2021client.data.modificarPermisos import ModificarPermisos

class ModificarPermisosPresentacion():
    """ Clase responsable de la interfaz correspondiente a la modificacion de permisos
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

    def modificarPermisos(self):
        """ Metodo que nos permite seleccionar un usuario y modificar (quitar o añadir) el permiso
        que deseemos. """

        print("\n_________________________________________________\n")
        print("Marca el nombre del usuario al que quieras dar o quitar un derecho y el número con el derecho.")
        print("\tAdminUsers = 1")
        print("\tAdminRights = 2")
        print("\tAdminSensors = 3")
        print("\tAdminRules = 4")
        print("\tViewReports = 5")
        print("\n")

        username: str = input('\tNombre de ususario a cambiar los derechos: ')
        right: int = int(input("\tDerecho: "))

        dar_quitar: int = int(input("\tDar derecho [1] o quitar derecho [2]: "))

        respuesta = ModificarPermisos(self.__auth_service, self.__username, self.__session_id).modificarPermisos(username, right, dar_quitar)

        if respuesta == True:
            print("\t\t\x1b[1;32m" + "¡¡El cambio de los permisos se hizo con éxito!!" + "\033[0;m")
        else:
            print("Permiso no modificado ha ocurrido un error")
