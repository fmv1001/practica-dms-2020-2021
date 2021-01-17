""" Sensor 2 class module.
"""

import subprocess
from .sensorAbs import Sensor


class SensorFile(Sensor):
    """ Clase responsable del sensor 2
    """

    def __init__(self, ruta):
        """ Initialization/constructor method.
        """

        self.__reglas = [1,1,1,1]
        self.__ruta = ruta
        self.__valores = {}
        self.__esxist:bool = False
        self.__memoriaArchivo = '0'
        self.__fechaMod = '-/-/-'
        self.__monitorizar()
        self.__monitorizar_reglas()

        return

    def __monitorizar(self):
        """ Monitoriza las reglas del sensor2 y las guarda en la varible correspondiente
        """

        #Regla 1
        try:
            #Regla 2
            memoria = int(subprocess.getoutput('stat ' + self.__ruta + ' | grep Size | awk \' {print $2 }\''))
            self.__memoriaArchivo = "{:.0f}".format(memoria)

            #Regla 3 
            fecha = subprocess.getoutput('stat ' + self.__ruta + ' | grep Modify | awk \' {print $2 }\'')
            self.__fechaMod = fecha
            self.__esxist = True

        except FileNotFoundError:
            self.__esxist = False
            self.__memoriaArchivo = '0'
            self.__fechaMod = '-/-/-'
            return
        except:
            self.__esxist = False
            self.__memoriaArchivo = '0'
            self.__fechaMod = '-/-/-'
            return
        return

    def __rellenar(self):
        """ Guarda el valor de las reglas del sensor en un diccionario
        """

        self.__valores["Ruta"] = self.__ruta
        self.__valores["Exist"] = self.__esxist
        self.__valores["MEM"] = self.__memoriaArchivo
        self.__valores["FECHAMOD"] = self.__fechaMod

        return

    def cambiar_reglas(self, regla):
        """ Monitoriza las reglas del sensor2
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
