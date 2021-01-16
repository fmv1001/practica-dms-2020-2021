import time, os
from getpass import getpass
from dms2021client.data.loginApp import LoginApp
from dms2021client.data.rest.exc import InvalidCredentialsError


class LoginAppPresentacion():

    def __init__(self, auth_service):
        self.__auth_service = auth_service
        return
    
    def login(self):
        """ Metodo que permite al usuario logearse. """

        while not self.__auth_service.is_running():
            os.system("clear")
            print("\x1b[1;36m" + "El servicio de autentificacion se esta iniciando, espere por favor.")
            time.sleep(0.5)
            os.system("clear")
            print("El servicio de autentificacion se esta iniciando, espere por favor..")
            time.sleep(0.5)
            os.system("clear")
            print("El servicio de autentificacion se esta iniciando, espere por favor..." + "\033[0;m")
            time.sleep(0.5)
        os.system("clear")
        print("\x1b[1;36m" + "\nAuthentication service up!")

        print("LOGIN -->")
        username: str = input('\tUsername: ' + "\033[0;m")
        password: str = getpass("\x1b[1;36m" + '\tPassword: ' + "\033[0;m")
        print("\033[0;m\n")
        try:
            session_id = LoginApp(self.__auth_service, username, password).login()
            print('\x1b[1;32m' + 'Logged in successfully!!' + "\033[0;m")
            time.sleep(1)
        except InvalidCredentialsError:
            print("\x1b[1;31m" + "Wrong username and/or password. Try again." + "\033[0;m")
            time.sleep(2)
            session_id, username = self.login()
        except Exception as ex:
            print(ex)
            
        return session_id, username