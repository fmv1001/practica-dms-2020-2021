""" ModificarPermisos class module.
"""
class ModificarPermisos():
    """ Clase responsable de mandar la orden de modificar los permisos de un usuario
    """

    def __init__(self, auth_service, username, session_id):
        """ Initialization/constructor method.
        """

        self.__auth_service = auth_service
        self.__username = username
        self.__session_id = session_id

    def modificarPermisos(self, username, right, dar_quitar) -> bool:
        """ Metodo que nos permite seleccionar un usuario y modificar (quitar o añadir) el permiso
        que deseemos.
        ---
        Parameters:
            - username: nombre de usuario a modificar permisos
            - right: derecho de usuario
            - dar_quitar: dar o quitar permiso a usuario
        Returns:
            True si el permiso se cambia con exito, False si no
        """

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
