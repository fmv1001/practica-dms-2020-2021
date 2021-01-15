from dms2021client.data.rest import SensorService
from dms2021client.data import consultarSensores

class ConsultarSensoresPresentacion():

    __sensor1_service: SensorService

    def __init__(self, sensor1_service: SensorService):
        self.__sensor1_service = sensor1_service

    def consultarSensoresExistentes(self):
        """ Método que nos permite seleccionar un sensor del que queramos obtener los datos. """

        print("\n\t_________________________________________________\n")
        print("\tEscoja el tipo de sensor a consultar ")
        print("\t\t[1] Sensor del sistema")
        print("\t\t[2] Sensor de un directorio")
        print("\n")
        print("\n\t\t...Consultando sensores...\n")
        dict_sensor =   consultarSensores.ConsultarSensores(self.__sensor1_service).consultarSensoresExistentes()

        if len(dict_sensor.keys()) == 0:
            print("Erorr")
        else: 
            print("\t\t\x1b[1;32m" + "¡¡Sensor consultado con éxito!!" + "\033[0;m")
            print("\t\t - Respuesta del sensor consultado:")
            for i in dict_sensor.keys():
                print("\t\t\t",i,"\t\t",dict_sensor[i])

        return 0