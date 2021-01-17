""" ConsultarSensores class module.
"""

from dms2021client.data.rest import SensorService

class ConsultarSensores():
    """ Clase responsable de mandar la orden de consultar los sensores
    """

    __sensor1_service: SensorService

    def __init__(self, sensor1_service: SensorService):
        """ Initialization/constructor method.
        """

        self.__sensor1_service = sensor1_service

    def consultarSensoresExistentes(self, tipo_sensor:str):
        """ Método que nos permite seleccionar un sensor del que queramos obtener los datos.
        ---
        Parameters:
            - tipo_sensor: tipo del sensor
        Returns:
            Diccionario con los valores de las reglas del sensor
        """

        if self.__sensor1_service.is_running() == True:
            dict_respuesta = self.__sensor1_service.consulta_sensor(tipo_sensor)
        else:
            dict_respuesta = {}

        return dict_respuesta
