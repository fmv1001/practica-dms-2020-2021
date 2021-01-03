from .sensorAbs import Sensor
import subprocess

class SensorFile(Sensor):

    def __init__(self, ruta):
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
        self.__valores["Ruta"] = self.__ruta
        self.__valores["Exist"] = self.__esxist
        self.__valores["MEM"] = self.__memoriaArchivo
        self.__valores["FECHAMOD"] = self.__fechaMod
        return

    def cambiar_reglas(self, regla):
        if int(regla) > 4 or int(regla) < 1:
            raise Exception
        if self.__reglas[int(regla)-1] == 1:
            self.__reglas[int(regla)-1] = 0
        else:
            self.__reglas[int(regla)-1] = 1
        self.__monitorizar_reglas()
        return
    
    def __monitorizar_reglas(self):
        self.__rellenar()
        eliminar_regla = []
        for i,key in enumerate(self.__valores.keys()):
            if self.__reglas[i] == 0:
                eliminar_regla.append(key)
        for key in eliminar_regla:
            self.__valores.pop(key)
        return
    
    def obtenerSensor(self): # -> dict
        return self.__valores

    def actualizarSensor(self):
        self.__monitorizar()
        self.__monitorizar_reglas()
        return

    def __str__(self):
        return 'Memoria usada del archivo' + str(self.__ruta) + ': ' + str(self.__memoriaArchivo) + 'MB'