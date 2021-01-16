from dms2021client.data.rest import SensorService
from dms2021client.data import cambiarReglas
from dms2021client.presentation.visualizacionSensor import sensorSTR

class CambiarReglasPresentacion():

    __sensor1_service: SensorService

    def __init__(self, sensor1_service: SensorService):
        self.__sensor1_service = sensor1_service
    
    def cambiarreglas(self):
        """ Método que actualiza las reglas de los sensores. """

        print("\n\t_________________________________________________\n")
        print("\tEscoja el tipo de sensor a actualizar sus reglas")
        print("\t\t[1] Sensor del sistema")
        print("\t\t[2] Sensor de un directorio")
        print("\n")

        tipo_sensor = str(input("\tEscoge el sensor que desees: "))
        regla = self.__menureglas(tipo_sensor)


        print("\n\t\t...Actualizando reglas...\n")
        dict_sensor = cambiarReglas.CambiarReglas(self.__sensor1_service).cambiarreglas(regla, tipo_sensor)

        if len(dict_sensor.keys()) == 0:
            print("Erorr")
        else: 
            print("\t\t\x1b[1;32m" + "¡¡Regla cambiada con éxito!!" + "\033[0;m")
            print("\t\t - Ahora la respuesta del sensor sera la siguiente:")
            sensorSTR(dict_sensor).mostrarSesnor()
  

        return 0

    def __menureglas(self, sensor:str):
        """ MUestra las reglas que se puedan actualizar y deja elegir al usuario. """

        if int(sensor)==1:
            print("\n\t_________________________________________________\n")
            print("\tEscoja la regla que quiere modificar")
            print("\t\t[1] RAM")
            print("\t\t[2] DISK")
            print("\t\t[3] SWAP")
            print("\t\t[4] CPU")
            print("\n")
            regla = str(input("\tEscoge la regla que desees: "))
        elif int(sensor)==2:
            print("\n\t_________________________________________________\n")
            print("\tEscoja la regla que quiere modificar")
            print("\t\t[1] RUTA")
            print("\t\t[2] EXIST")
            print("\t\t[3] MEM")
            print("\t\t[4] FECHAMOD")
            print("\n")
            regla = str(input("\tEscoge la regla que desees: "))
        return regla