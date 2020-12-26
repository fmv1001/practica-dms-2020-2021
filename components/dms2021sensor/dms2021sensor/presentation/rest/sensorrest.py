from dms2021sensor.logic.sensor1 import SensorMem
#from dms2021auth.logic import UserManager
from dms2021core.data.rest import RestResponse
import json

class RestSensor():
    def __init__(self):
        self.__sensor = SensorMem()
        return

    def monitorizarSensor(self, sensor_type : str) -> RestResponse:
        try:
            if int(sensor_type)==1:
                resultado = self.__sensor.obtenerSensor()
                resultado_json = json.dumps(resultado)
            elif int(sensor_type)==2:
                resultado = 'Sensor 2 no implementado, en proximas actualizaciones...'
            else:
                resultado = 'Sensor 3 no implementado, en proximas actualizaciones...'
        except ValueError:
            return RestResponse(code=400,mime_type='text/plain')

        return RestResponse(resultado_json , 200, mime_type='text/plain')
    
    def actualizar_sensor(self, sensor_type : str) -> RestResponse:
        try:
            if int(sensor_type)==1:
                self.__sensor.actualizarSensor()
                resultado = self.__sensor.obtenerSensor()
                resultado_json = json.dumps(resultado)
            elif int(sensor_type)==2:
                resultado = 'Sensor 2 no implementado, en proximas actualizaciones...'
            else:
                resultado = 'Sensor no implementado, en proximas actualizaciones...'
        except ValueError:
            return RestResponse(code=400,mime_type='text/plain')

        return RestResponse(resultado_json , 200, mime_type='text/plain')
