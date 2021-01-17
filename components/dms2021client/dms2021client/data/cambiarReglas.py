""" CambiarReglas class module.
"""

from dms2021client.data.rest import SensorService

class CambiarReglas():
    """ Clase responsable de mandar la orden de cambiar las reglas de algun sensor
    """

    __sensor1_service: SensorService

    def __init__(self, sensor1_service: SensorService):
        """ Initialization/constructor method.
        """

        self.__sensor1_service = sensor1_service

    def cambiarreglas(self, regla, tipo_sensor) -> dict:
        """ Método que cambia las reglas de los sensores.
        ---
        Parameters:
            - regla: regla a cambiar
            - tipo_sensor: tipo del sensor
        Returns:
            Diccionario con los valores de las reglas del sensor
        """

        if self.__sensor1_service.is_running() == True:
            dict_respuesta = self.__sensor1_service.actualizarlasreglas(tipo_sensor, regla)
        else:
            dict_respuesta = {}

        return dict_respuesta
