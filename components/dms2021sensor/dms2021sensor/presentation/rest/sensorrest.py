""" RestSensor class module.
"""

import json
from dms2021sensor.logic.sensor1 import SensorMem
from dms2021sensor.logic.sensor2 import SensorFile
from dms2021core.data.rest import RestResponse

class RestSensor():
    """ Class responsible of handling the sensor-related REST requests.
    """
    def __init__(self):
        """ Initialization/constructor method.
        """

        self.__sensor1 = SensorMem()
        self.__sensor2 = SensorFile('/home')

        return

    def monitorizarSensor(self, sensor_type : str) -> RestResponse:
        """ Extrae los resultados del sensor
        ---
        Parameters:
            - sensor_type: Tipo del sensor.
        Returns:
            A RestResponse object holding the result of the operation.
        """

        try:
            if int(sensor_type)==1:
                resultado = self.__sensor1.obtenerSensor()
                resultado_json = json.dumps(resultado)
            elif int(sensor_type)==2:
                resultado = self.__sensor2.obtenerSensor()
                resultado_json = json.dumps(resultado)
            else:
                resultado = 'Sensor no implementado, en proximas actualizaciones...'
        except ValueError:
            return RestResponse(code=400,mime_type='text/plain')

        return RestResponse(resultado_json , 200, mime_type='text/plain')

    def actualizar_sensor(self, sensor_type : str) -> RestResponse:
        """ Manda una orden para actucalizar los resultados del sensor
        ---
        Parameters:
            - sensor_type: Tipo del sensor.
        Returns:
            A RestResponse object holding the result of the operation.
        """

        try:
            if int(sensor_type)==1:
                self.__sensor1.actualizarSensor()
                resultado = self.__sensor1.obtenerSensor()
                resultado_json = json.dumps(resultado)
            elif int(sensor_type)==2:
                self.__sensor2.actualizarSensor()
                resultado = self.__sensor2.obtenerSensor()
                resultado_json = json.dumps(resultado)
            else:
                resultado = 'Sensor no implementado, en proximas actualizaciones...'
        except ValueError:
            return RestResponse(code=400,mime_type='text/plain')

        return RestResponse(resultado_json , 200, mime_type='text/plain')

    def actualizar_reglas(self, sensor_type : str, regla: str) -> RestResponse:
        """ Manda una orden para cambiar las reglas de un sensor
        ---
        Parameters:
            - sensor_type: Tipo del sensor.
            - regla: regla a cambiar del sensor
        Returns:
            A RestResponse object holding the result of the operation.
        """

        try:
            if int(sensor_type)==1:
                self.__sensor1.cambiar_reglas(regla)
                resultado = self.__sensor1.obtenerSensor()
                resultado_json = json.dumps(resultado)
            elif int(sensor_type)==2:
                self.__sensor2.cambiar_reglas(regla)
                resultado = self.__sensor2.obtenerSensor()
                resultado_json = json.dumps(resultado)
            else:
                resultado = 'Sensor no implementado, en proximas actualizaciones...'
        except ValueError:
            return RestResponse(code=400,mime_type='text/plain')

        return RestResponse(resultado_json , 200, mime_type='text/plain')
