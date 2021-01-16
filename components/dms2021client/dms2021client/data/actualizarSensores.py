from dms2021client.data.rest import SensorService

class ActualizarSensores():

    __sensor1_service: SensorService

    def __init__(self, sensor1_service: SensorService):
        self.__sensor1_service = sensor1_service

    def actualizarSensoresExistentes(self, tipo_sensor:str) -> dict:
        """ Método que actualiza el valor que devuelven los sensores. """

        

        if self.__sensor1_service.is_running() == True:
            dict_respuesta = self.__sensor1_service.actualizar_sensor(tipo_sensor)
        else:
            dict_respuesta = {}

        return dict_respuesta
