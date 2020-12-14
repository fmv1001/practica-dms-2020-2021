from sensorAbs import Sensor
import commands

class SensorSwap(Sensor):

    def __init__(self):
        self.__swap = 0
        self.__calcularSwap()
        return

    def __calcularSwap(self):
        SwapTotal=commands.getoutput('grep SwapTotal /proc/meminfo | awk \' {print $2 }\' ')
        SwapFree=commands.getoutput('grep SwapFree /proc/meminfo | awk \' {print $2 }\' ')
        ##mem.ocupada=mem.total-mem.libre
        Swap=(int(SwapTotal) - int(SwapFree))*100/int(SwapTotal)
        self.__swap = Swap
        return
    
    def obtenerSwap(self): # -> int
        return self.__swap

    def actualizarSwapSensor(self):
        self.__calcularSwap()
        return

    def __str__(self):
        return 'Memoria swap usada del sistema: ' + str(self.obtenerSwap()) + '%'