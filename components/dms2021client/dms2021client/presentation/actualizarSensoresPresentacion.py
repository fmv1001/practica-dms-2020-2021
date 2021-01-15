from dms2021client.data import actualizarSensores
from dms2021client.data.rest import SensorService

class ActualizarSensoresPresentacion():

    def __init__(self, sensor1_service: SensorService):
        self.__sensor1_service = sensor1_service

    def actualizarSensoresExistentes(self):
        """ Método que actualiza el valor que devuelven los sensores. """

        print("\n\t_________________________________________________\n")
        print("\tEscoja el tipo de sensor a actualizar ")
        print("\t\t[1] Sensor del sistema")
        print("\t\t[2] Sensor de un directorio")
        print("\n")
        print("\n\t\t...Actualizando sensores...\n")
        dict_sensor = actualizarSensores.ActualizarSensores(self.__sensor1_service).actualizarSensoresExistentes()

        if len(dict_sensor.keys()) == 0:
            print("Erorr")
        else: 
            print("\t\t\x1b[1;32m" + "¡¡Sensor actualizado con éxito!!" + "\033[0;m")
            print("\t\t - Respuesta del sensor actualizado:")
            for i in dict_sensor.keys():
                print("\t\t\t",i,"\t\t",dict_sensor[i])


        return 0
