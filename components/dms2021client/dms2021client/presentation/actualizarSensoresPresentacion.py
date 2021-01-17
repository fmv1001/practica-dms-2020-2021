""" ActualizarSensoresPresentacion class module.
"""

from dms2021client.data.actualizarSensores import ActualizarSensores
from dms2021client.data.rest import SensorService
from dms2021client.presentation.visualizacionSensor import sensorSTR

class ActualizarSensoresPresentacion():
    """ Clase responsable de la interfaz correspondiente a actualizar un sensor
    """

    def __init__(self, sensor1_service: SensorService):
        """ Initialization/constructor method.
        """

        self.__sensor1_service = sensor1_service

    def actualizarSensoresExistentes(self):
        """ Método que actualiza el valor que devuelven los sensores.
        """

        print("\n\t_________________________________________________\n")
        print("\tEscoja el tipo de sensor a actualizar ")
        print("\t\t[1] Sensor del sistema")
        print("\t\t[2] Sensor de un directorio")
        print("\n")

        tipo_sensor = str(input("\tEscoge el sensor que desees: "))

        print("\n\t\t...Actualizando sensores...\n")
        dict_sensor = ActualizarSensores(self.__sensor1_service).actualizarSensoresExistentes(tipo_sensor)

        if len(dict_sensor.keys()) == 0:
            print("Erorr")
        else:
            print("\t\t\x1b[1;32m" + "¡¡Sensor actualizado con éxito!!" + "\033[0;m")
            print("\t\t - Respuesta del sensor actualizado:")
            sensorSTR(dict_sensor).mostrarSesnor()
