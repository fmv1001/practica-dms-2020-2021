from psutil import disk_usage, cpu_percent
from .sensorAbs import Sensor
import subprocess

class SensorMem(Sensor):

    def __init__(self):
        self.__valores = {}
        self.__memUsada = '0'
        self.__swap = '0'
        self.__disk = '0'
        self.__CPU = '0'
        self.__monitorizar()
        self.__rellenar()
        return

    def __monitorizar(self):
        #Regla 1
        result1 = subprocess.getoutput('grep MemTotal /proc/meminfo | awk \' {print $2 }\' ')
        result2 = subprocess.getoutput('grep MemAvailable /proc/meminfo | awk \' {print $2 }\' ')
        mem_usada = 100 - (int(result2)*100/int(result1))
        self.__memUsada = "{:.2f}".format(mem_usada)

        #Regla 2
        swap_total=subprocess.getoutput('grep SwapTotal /proc/meminfo | awk \' {print $2 }\' ')
        swap_free=subprocess.getoutput('grep SwapFree /proc/meminfo | awk \' {print $2 }\' ')
        ##mem.ocupada=mem.total-mem.libre
        swap_used = (int(swap_total) - int(swap_free))*100/int(swap_total)
        self.__swap = "{:.2f}".format(swap_used)

        #Regla 3 
        disk_used = disk_usage("/")
        self.__disk = str(disk_used.percent)

        #Regla 4 
        self.__CPU = cpu_percent(interval=4)

        return
    
    def __rellenar(self):
        self.__valores["RAM"] = self.__memUsada
        self.__valores["SWAP"] = self.__swap
        self.__valores["DISK"] = self.__disk
        self.__valores["CPU"] = self.__CPU
        return



    """
    def __B2GB(self, bytes):
        "Convertidor de bytes a gigabytes."
        return bytes / 1024**3
    """
    
    def obtenerSensor(self): # -> dict
        return self.__valores

    def actualizarSensor(self):
        self.__monitorizar()
        self.__rellenar()
        return

    def __str__(self):
        return 'Memoria usada del sistema: ' + str(self.obtenerSensor()) + '%'