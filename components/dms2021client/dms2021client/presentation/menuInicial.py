import os

class MenuLogInicial():
    
    def __init__(self):
        pass

    def menuLogInOrExit(self):
        """Metodo inicial en el que se le da la posibilidad al usuario de logearse o salir. """

        os.system("clear")

        print("\x1b[1;36m" + "+-----------------------------------------------------------------------+")
        print("| MENU INICIAL -->                                        appGuilleFran"+ chr(174)+"|")
        print("+-----------------------------------------------------------------------+")
        print("|        1.Log in.                                                      |")
        print("|        2.Salir del programa.                                          |")
        print("+-----------------------------------------------------------------------+")
        print('\033[0;m' + "\n")


        salida: int = 0
        while(salida < 1 or salida > 2):
            salida: int = int(input('\033[1;37m' + "\tEscoja la opción que desee: " + '\033[0;m'))
            if(salida >2 or salida < 1):
                print("\x1b[1;33m" + "ERROR --> " + '\033[0;m' + "Porfavor introduce una opción de entre las que se encuentren disponibles.")

        return salida
