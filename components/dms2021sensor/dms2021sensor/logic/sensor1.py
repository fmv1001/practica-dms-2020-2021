""" Sensor 1 class module.
"""
import subprocess
from psutil import disk_usage, cpu_percent
from .sensorAbs import Sensor

class SensorMem(Sensor):
    """ Clase responsable del sensor 1
    """

    def __init__(self):
        """ Initialization/constructor method.
        """

        self.__reglas = [1,0,1,0]
        self.__valores = {}
        self.__memUsada = '0'
        self.__swap = '0'
        self.__disk = '0'
        self.__CPU = '0'
        self.__monitorizar()
        self.__monitorizar_reglas()

        return

    def __monitorizar(self):
        """ Monitoriza las reglas del sensor1 y las guarda en la varible correspondiente
        """

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
        """ Guarda el valor de las reglas del sensor en un diccionario
        """

        self.__valores["RAM"] = self.__memUsada
        self.__valores["SWAP"] = self.__swap
        self.__valores["DISK"] = self.__disk
        self.__valores["CPU"] = self.__CPU

        return

    def cambiar_reglas(self, regla):
        """ Monitoriza las reglas del sensor1
        ---
        Parameters:
            - regla: regla que se desea cambiar
        """
        if int(regla) > 4 or int(regla) < 1:
            raise Exception
        if self.__reglas[int(regla)-1] == 1:
            self.__reglas[int(regla)-1] = 0
        else:
            self.__reglas[int(regla)-1] = 1
        self.__monitorizar_reglas()
        return

    def __monitorizar_reglas(self):
        """ Elimna del diccionario las entradas que no son visibles al usuario
        """

        self.__rellenar()
        eliminar_regla = []
        for i,key in enumerate(self.__valores.keys()):
            if self.__reglas[i] == 0:
                eliminar_regla.append(key)
        for key in eliminar_regla:
            self.__valores.pop(key)

        return

    def obtenerSensor(self):
        """ Devuelve el diccionario con los valores del sensor
        ---
        Returns:
            Diccionario con los valores del sensor
        """

        return self.__valores

    def actualizarSensor(self):
        """ Actualiza los valores del sensor
        """

        self.__monitorizar()
        self.__monitorizar_reglas()

        return
