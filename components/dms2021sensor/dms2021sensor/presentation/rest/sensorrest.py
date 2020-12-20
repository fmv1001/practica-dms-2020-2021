from dms2021sensor.logic.sensor1 import SensorMem
#from dms2021auth.logic import UserManager
from dms2021core.data.rest import RestResponse

class RestSensor():
    def __init__(self):
        return

    def monitorizarSensor(self, sensor_type : str) -> RestResponse:
        try:
            if int(sensor_type)==1:
                sensor = SensorMem()
        except ValueError:
            return RestResponse(code=400,mime_type='text/plain')
        except:
            return RestResponse(code=501,mime_type='text/plain')

        return RestResponse(print(sensor), 200, mime_type='text/plain')
