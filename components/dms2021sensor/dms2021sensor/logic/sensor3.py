#
from .sensorAbs import Sensor
import subprocess

class SensorArchivoX(Sensor):

    def __init__(self, ruta):
        self.__ruta = ruta
        self.__memoriaArchivo = 0
        self.__tipoMem = 'K'
        self.__monitorizar()
        return

    def __monitorizar(self):
        try:
            memoria=subprocess.getoutput('du -sh ' + self.__ruta + ' | awk \' {print $1 }\'')
            memoria = str(memoria)
            self.__tipoMem = memoria[-1]
            memoria = memoria[:-1]
            self.__memoriaArchivo = memoria
        except:
            print("No existe el archivo o ha ocurrido algun error")
        return
    
    def obtenerSensor(self): # -> int
        return self.__memoriaArchivo

    def obtenerRuta(self): # -> int
        return self.__ruta

    def actualizarSensor(self, ruta):
        self.__ruta = ruta
        self.__monitorizar()
        return

    def __str__(self):
        return 'Memoria del archivo ' + str(self.__ruta) + ': ' + str(self.__memoriaArchivo) + ' '+ str(self.__tipoMem) + 'B'