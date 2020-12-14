from dms2021sensor.logic.sensor1 import SensorMem
from dms2021auth.logic import UserManager

class sensorService():
    def __init__(self):
        pass

    def create(self, sensor_type : int) -> RestResponse:
        try:
            sensor = SensorMem()
        except ValueError:
            pass

        return RestResponse(sensor.obtenerMemUsada())
