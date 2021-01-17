""" CambiarReglas class module.
"""
from dms2021client.data.rest import AuthService
from dms2021client.data.rest import SensorService
from dms2021client.data.rest.exc import InvalidCredentialsError, UnauthorizedError

class CambiarReglas():
    """ Clase responsable de mandar la orden de cambiar las reglas de algun sensor
    """

    __sensor1_service: SensorService
    __auth_service: AuthService

    def __init__(self, sensor1_service: SensorService, auth_service: AuthService):
        """ Initialization/constructor method.
        """

        self.__sensor1_service = sensor1_service
        self.__auth_service = auth_service

    def cambiarreglas(self, regla, tipo_sensor, username) -> dict:
        """ Método que cambia las reglas de los sensores.
        ---
        Parameters:
            - regla: regla a cambiar
            - tipo_sensor: tipo del sensor
        Returns:
            Diccionario con los valores de las reglas del sensor
        """
        if self.__auth_service.is_running() == True:
            status = self.__auth_service.has_right(username, 'AdminRules')
            if status == 200:
                if self.__sensor1_service.is_running() == True:
                    dict_respuesta = self.__sensor1_service.actualizarlasreglas(tipo_sensor, regla)
                else:
                    dict_respuesta = {}

                return dict_respuesta    
            elif status == 404:
                raise UnauthorizedError()
            else:
                print("ERROR: ....", status)
                raise Exception
        return {}
    
