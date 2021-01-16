
class ModificarPermisos():

    def __init__(self, auth_service, username, session_id):
        self.__auth_service = auth_service
        self.__username = username
        self.__session_id = session_id
        return

    def modificarPermisos(self, username, right, dar_quitar) -> bool:
        """ Metodo que nos permite seleccionar un usuario y modificar (quitar o añadir) el permiso
        que deseemos. """
        
        if dar_quitar == 1:
            status = self.__auth_service.dar_quitar_permisos(self.__username, username, right, self.__session_id, 'POST')
            if status == 200:
                salida = True
            else:
                salida = False
        else:
            status = self.__auth_service.dar_quitar_permisos(self.__username, username, right, self.__session_id, 'DELETE')
            if status == 200:
                salida = True
            else:
                salida = False
        
        return salida
        