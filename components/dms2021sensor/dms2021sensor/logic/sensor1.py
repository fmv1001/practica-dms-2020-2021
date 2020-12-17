
from .sensorAbs import Sensor
import subprocess

class SensorMem(Sensor):

    def __init__(self):
        self.__memUsada = 0
        self.__monitorizar()
        return

    def __monitorizar(self):
        result1 = subprocess.getoutput('grep MemTotal /proc/meminfo | awk \' {print $2 }\' ')
        result2 = subprocess.getoutput('grep MemAvailable /proc/meminfo | awk \' {print $2 }\' ')
        mem_usada = 100 - (int(result2)*100/int(result1))
        self.__memUsada = mem_usada
        return
    
    def obtenerSensor(self): # -> int
        return self.__memUsada

    def actualizarSensor(self):
        self.__monitorizar()
        return
    
    def copy(self):
        return SensorMem()

    def __str__(self):
        return 'Memoria usada del sistema: ' + str(self.obtenerSensor()) + '%'