from dms2021client.data.rest import AuthService

class ModificarPermisos():

    __session_id: str
    __username: str
    __auth_service: AuthService

    def __init__(self, session_id: str, username: str, auth_service: AuthService):
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
        if dar_quitar == 1:
            self.__auth_service.dar_quitar_permisos(self.__username, username, right, self.__session_id, 'POST')
        else:
            self.__auth_service.dar_quitar_permisos(self.__username, username, right, self.__session_id, 'DELETE')
        return 0
        