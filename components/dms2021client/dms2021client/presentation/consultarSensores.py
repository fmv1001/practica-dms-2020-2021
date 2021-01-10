from dms2021client.data.rest import SensorService

class ConsultarSensores():

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

        tipo_sensor = str(input("\tEscoge el sensor que desees: "))

        if self.__sensor1_service.is_running() == True:
            print("\n\t\t...Obteniendo datos...\n")
            dict_respuesta = self.__sensor1_service.consulta_sensor(tipo_sensor)
            print("\t\t - Respuesta del sensor:")
            for i in dict_respuesta.keys():
                print("\t\t\t",i,"\t\t",dict_respuesta[i])
            #print("\t\t\t",dict_respuesta)
        else:
            print("\n\tSE HA PRODUCIDO UN ERROR AL INICIAR EL SENSOR")

        return 0
