#!/usr/bin/env python3

import time
from getpass import getpass
from dms2021client.data.config import ClientConfiguration
from dms2021client.data.rest import AuthService
from dms2021client.data.rest import SensorService
from dms2021client.data.rest.exc import InvalidCredentialsError, UnauthorizedError
from dms2021client.presentation import menuOpciones, menuPrincipal, crearUsuario, modificarPermisos, consultarSensores,actualizarSensores
from dms2021client.presentation.logoutService import  Exit

class LanzadorCliente():

    __session_id: str
    __username: str
    __auth_service: AuthService
    __cfg: ClientConfiguration
    __sensor_service: SensorService

    def __init__(self):
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
        actualizacion = actualizarSensores.ActualizarSensores(self.__sensor1_service)

        while True:
            menu_principal = menuPrincipal.MenuLogPrincipal()
            salida: int = menu_principal.menuLogInOrExit()

            if salida == 1:
                self.__session_id, self.__username = self.login()
                while True:
                    salida_pantalla = menuOpciones.MenuDeOpciones()
                    respuesta = salida_pantalla.menu()

                    if respuesta == 0:
                        salir_programa = Exit(self.__session_id, self.__auth_service)
                        if salir_programa.exitPagina() == -1:
                            break
                    elif respuesta == 1:
                        crear_usuario = crearUsuario.CrearUsuario(self.__session_id, self.__username, self.__auth_service)
                        crear_usuario.creacionUsuario()
                    elif respuesta == 2:
                        modificar_permisos = modificarPermisos.ModificarPermisos(self.__session_id, self.__username, self.__auth_service)
                        modificar_permisos.modificarPermisos()
                    elif respuesta == 3:
                        consulta = consultarSensores.ConsultarSensores(self.__sensor1_service)
                        consulta.consultarSensoresExistentes()
                    elif respuesta == 4:
                        actualizacion.actualizarSensoresExistentes()
                    elif respuesta == 5:
                        actualizacion.cambiarreglas()
                    print("\t_________________________________________________")
                    input('\n\t\tIntro para continuar ...')

            elif salida == 2:
                print("\n"+"\x1b[1;33m" + "+----------------------------+")
                print("| SALIENDO DEL PROGRAMA      |")
                print("+----------------------------+" + '\033[0;m')

                break

    def login(self):
        """ Metodo que permite al usuario logearse. """

        while not self.__auth_service.is_running():
            time.sleep(1)
        print("\nAuthentication service up!")

        print("LOGIN -->")
        username: str = input('\tUsername: ')
        password: str = getpass('\tPassword: ')
        try:
            self.__session_id: str = self.__auth_service.login(username, password)
            self.__username = username
            print('Logged in successfully as ' + username + ' . Session id: ' + self.__session_id)
        except InvalidCredentialsError:
            print('Wrong username and/or password. Try again.')
            self.__session_id, self.__username = self.login()
        except Exception as ex:
            print(ex)

        return self.__session_id, self.__username

LanzadorCliente()