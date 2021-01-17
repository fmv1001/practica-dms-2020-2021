#!/usr/bin/env python3
""" InterfazPorMenues class module.
"""

import time 
import os
from dms2021client.data.config import ClientConfiguration
from dms2021client.data.rest import AuthService
from dms2021client.data.rest import SensorService
from dms2021client.presentation.loginAppPresentacion import LoginAppPresentacion
from dms2021client.presentation.menuPrincipal import MenuPrincipal
from dms2021client.presentation.menuInicial import MenuLogInicial
from dms2021client.presentation.modificarPermisosPresentacion import ModificarPermisosPresentacion
from dms2021client.presentation.actualizarSensoresPresentacion import ActualizarSensoresPresentacion
from dms2021client.presentation.consultarSensoresPresentacion import ConsultarSensoresPresentacion
from dms2021client.presentation.cambiarReglasPresentacion import CambiarReglasPresentacion
from dms2021client.presentation.crearUsuarioPresentacion import CrearUsuarioPresentacion
from dms2021client.presentation.logoutAppPresentacion import  ExitPresentacion

class InterfazPorMenues():
    """ Clase responsable de la interfaz correspondiente a la aplicacion
    """

    __session_id: str
    __username: str
    __auth_service: AuthService
    __cfg: ClientConfiguration
    __sensor_service: SensorService

    def __init__(self):
        """ Initialization/constructor method.
        """

        os.system("clear")
        print("\x1b[1;35m" + "+------------------+")
        print("| ¡¡BIENVENIDO!!   |")
        print("+------------------+" + '\033[0;m')
        print("\n\tEl programa se está iniciando.....")
        time.sleep(2)

        self.__cfg= ClientConfiguration()
        self.__cfg.load_from_file(self.__cfg.default_config_file())
        self.__auth_service = AuthService(self.__cfg.get_auth_service_host(), self.__cfg.get_auth_service_port())
        self.__sensor1_service = SensorService(self.__cfg.get_sensor_service_host(),self.__cfg.get_sensor_service_port())
        self.__sensor2_service = SensorService(self.__cfg.get_sensor2_service_host(),self.__cfg.get_sensor2_service_port())

        salir:int = 0
        while True:
            if salir != 1:
                menu_principal = MenuLogInicial()
                salida: int = menu_principal.menuLogInOrExit()

            if salida == 1:
                self.__session_id, self.__username = LoginAppPresentacion(self.__auth_service).login()
                while True:
                    salida_pantalla = MenuPrincipal()
                    respuesta = salida_pantalla.menu()

                    if respuesta == 0:
                        logout = ExitPresentacion(self.__session_id, self.__auth_service)
                        logout.exitPagina()
                        salir = 1
                        salida = 2
                        break
                    elif respuesta == 1:
                        crear_usuario = CrearUsuarioPresentacion(self.__session_id, self.__username, self.__auth_service)
                        crear_usuario.creacionUsuario()
                    elif respuesta == 2:
                        modificar_permisos = ModificarPermisosPresentacion(self.__session_id, self.__username, self.__auth_service)
                        modificar_permisos.modificarPermisos()
                    elif respuesta == 3:
                        consulta = ConsultarSensoresPresentacion(self.__sensor1_service)
                        consulta.consultarSensoresExistentes()
                    elif respuesta == 4:
                        actualizacion = ActualizarSensoresPresentacion(self.__sensor1_service)
                        actualizacion.actualizarSensoresExistentes()
                    elif respuesta == 5:
                        reglas = CambiarReglasPresentacion(self.__sensor1_service, self.__auth_service, self.__username)
                        reglas.cambiarreglas()
                    elif respuesta ==6:
                        logout = ExitPresentacion(self.__session_id, self.__auth_service)
                        if logout.exitPagina() == -1:
                            break
                    print("\t_________________________________________________")
                    input('\n\t\tIntro para continuar ...')

            elif salida == 2:
                print("\n" + "\x1b[1;33m" + "+----------------------------+")
                print("| SALIENDO DEL PROGRAMA      |")
                print("+----------------------------+" + '\033[0;m')

                break


InterfazPorMenues()
