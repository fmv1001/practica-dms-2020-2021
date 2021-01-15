
class ModificarPermisos():

    def __init__(self):
        return

    def modificarPermisos(self, auth_service, __username, __session_id) -> bool:
        """ Metodo que nos permite seleccionar un usuario y modificar (quitar o añadir) el permiso
        que deseemos. """

        username: str = input('\tNombre de ususario a cambiar los derechos: ')
        right: int = int(input("\tDerecho: "))

        dar_quitar: int = int(input("\tDar derecho [1] o quitar derecho [2]: "))
        if dar_quitar == 1:
            status = auth_service.dar_quitar_permisos(__username, username, right, __session_id, 'POST')
            if status == 200:
                salida = True
            else:
                salida = False
        else:
            status = auth_service.dar_quitar_permisos(__username, username, right, __session_id, 'DELETE')
            if status == 200:
                salida = True
            else:
                salida = False
        
        return salida
        