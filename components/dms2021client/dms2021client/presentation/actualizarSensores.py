from dms2021client.data.rest import SensorService

class ActualizarSensores():

    __sensor1_service: SensorService

    def __init__(self, sensor1_service: SensorService):
        self.__sensor1_service = sensor1_service

    def actualizarSensoresExistentes(self):
        """ Método que actualiza el valor que devuelven los sensores. """

        print("\n\t_________________________________________________\n")
        print("\tEscoja el tipo de sensor a actualizar ")
        print("\t\t[1] Sensor del sistema")
        print("\t\t[2] Sensor de un directorio")
        print("\n")

        tipo_sensor = str(input("\tEscoge el sensor que desees: "))

        if self.__sensor1_service.is_running() == True:
            print("\n\t\t...Actualizando sensores...\n")
            dict_respuesta = self.__sensor1_service.actualizar_sensor(tipo_sensor)
            print("\t\t - Respuesta del sensor:")
            for i in dict_respuesta.keys():
                print("\t\t\t",i,"\t\t",dict_respuesta[i])
            #print("\t\t\t",dict_respuesta)
        else:
            print("\n\tSE HA PRODUCIDO UN ERROR AL INICIAR EL SENSOR")

        return 0

    def cambiarreglas(self):
        """ Método que actualiza las reglas de los sensores. """

        print("\n\t_________________________________________________\n")
        print("\tEscoja el tipo de sensor a actualizar sus reglas")
        print("\t\t[1] Sensor del sistema")
        print("\t\t[2] Sensor de un directorio")
        print("\n")

        tipo_sensor = str(input("\tEscoge el sensor que desees: "))
        regla = self.menureglas(tipo_sensor)

        if self.__sensor1_service.is_running() == True:
            print("\n\t\t...Actualizando reglas...\n")
            dict_respuesta = self.__sensor1_service.actualizarlasreglas(tipo_sensor, regla)
            print("\t\t - Respuesta del sensor:")
            for i in dict_respuesta.keys():
                print("\t\t\t",i,"\t\t",dict_respuesta[i])
            #print("\t\t\t",dict_respuesta)
        else:
            print("\n\tSE HA PRODUCIDO UN ERROR AL INICIAR EL SENSOR")

        return 0

    def menureglas(self, sensor:str):
        """ MUestra las reglas que se puedan actualizar y deja elegir al usuario. """

        if int(sensor)==1:
            print("\n\t_________________________________________________\n")
            print("\tEscoja la regla que quiere modificar")
            print("\t\t[1] RAM")
            print("\t\t[2] DISK")
            print("\t\t[3] SWAP")
            print("\t\t[3] CPU")
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
