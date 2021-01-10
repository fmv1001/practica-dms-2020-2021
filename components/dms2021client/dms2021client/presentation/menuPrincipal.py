import os

class MenuLogPrincipal():
    
    def __init__(self):
        pass

    def menuLogInOrExit(self):
        """Metodo principal en el que se le da la posibilidad al usuario de logearse o salir. """

        os.system("clear")
        print("Selecciona la opción que desees, logearte con un usuario o salir del programa -->")
        print("\t1-Log In")
        print("\t2-Salir del programa\n")
        salida: int = 0
        while(salida < 1 or salida > 2):
            salida: int = int(input("\tEscoja la opción que desee: "))
            if(salida >2 or salida < 1):
                print("ERROR --> Porfavor introduce una opción de entre las que se encuentren disponibles.")

        return salida
