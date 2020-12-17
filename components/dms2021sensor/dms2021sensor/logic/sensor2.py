from .sensorAbs import Sensor
import subprocess

class SensorSwap(Sensor):

    def __init__(self):
        self.__swap = 0
        self.__monitorizar()
        return

    def __monitorizar(self):
        swap_total=subprocess.getoutput('grep SwapTotal /proc/meminfo | awk \' {print $2 }\' ')
        swap_free=subprocess.getoutput('grep SwapFree /proc/meminfo | awk \' {print $2 }\' ')
        ##mem.ocupada=mem.total-mem.libre
        swap=(int(swap_total) - int(swap_free))*100/int(swap_total)
        self.__swap = swap
        return
    
    def obtenerSensor(self): # -> int
        return self.__swap

    def actualizarSensor(self):
        self.__monitorizar()
        return

    def __str__(self):
        return 'Memoria swap usada del sistema: ' + str(self.obtenerSensor()) + '%'