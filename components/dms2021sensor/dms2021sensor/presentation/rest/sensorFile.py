from dms2021sensor.logic.sensor1 import SensorMem
#from dms2021auth.logic import UserManager
from dms2021core.data.rest import RestResponse

class sensorService():
    def __init__(self):
        return

    def monitorizarSensor(self, sensor_type : int) -> RestResponse:
        try:
            if sensor_type==1:
                sensor = SensorMem()
                print(sensor)
        except ValueError:
            return RestResponse(code=400,mime_type='text/plain')

        return RestResponse(sensor.obtenerSensor(), 200, mime_type='text/plain')
