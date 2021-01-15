from dms2021client.data.rest import SensorService

class CambiarReglas():

    __sensor1_service: SensorService

    def __init__(self, sensor1_service: SensorService):
        self.__sensor1_service = sensor1_service   
    
    
    
    def cambiarreglas(self, regla, tipo_sensor) -> dict:
        """ Método que actualiza las reglas de los sensores. """

        if self.__sensor1_service.is_running() == True:
            dict_respuesta = self.__sensor1_service.actualizarlasreglas(tipo_sensor, regla)
        else:
            dict_respuesta = {}

        return dict_respuesta