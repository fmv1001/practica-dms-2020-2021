
from .sensorAbs import Sensor
import commands

class SensorMem(Sensor):

    def __init__(self):
        self.__memUsada = 0
        self.__monitorizar()
        return

    def __monitorizar(self):
        result1 = commands.getoutput('grep MemTotal /proc/meminfo | awk \' {print $2 }\' ')
        result2 = commands.getoutput('grep MemAvailable /proc/meminfo | awk \' {print $2 }\' ')
        memUsada = 100 - (int(result2)*100/int(result1))
        self.__memUsada = memUsada
        return
    
    def obtenerMemUsada(self): # -> int
        return self.__memUsada

    def actualizarMemUsadaSensor(self):
        self.__monitorizar()
        return
    
    def copy(self):
        return SensorMem()

    def __str__(self):
        return 'Memoria usada del sistema: ' + str(self.obtenerMemUsada()) + '%'