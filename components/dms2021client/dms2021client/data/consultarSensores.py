from dms2021client.data.rest import SensorService

class ConsultarSensores():

    __sensor1_service: SensorService

    def __init__(self, sensor1_service: SensorService):
        self.__sensor1_service = sensor1_service

    def consultarSensoresExistentes(self, tipo_sensor:str):
        """ Método que nos permite seleccionar un sensor del que queramos obtener los datos. """

        if self.__sensor1_service.is_running() == True:
            dict_respuesta = self.__sensor1_service.consulta_sensor(tipo_sensor)
        else:
            dict_respuesta = {}

        return dict_respuesta
