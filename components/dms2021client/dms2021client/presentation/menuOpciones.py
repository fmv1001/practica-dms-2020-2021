import os
class menuDeOpciones():

    def __init__(self):
        return

    def menu(self):
        os.system("clear")
        print("\x1b[1;36m" + "+-----------------------------------------------------------------------+")
        print("| MENU PRINCIPAL -->                                      appGuilleFran"+ chr(174)+"|")
        print("+-----------------------------------------------------------------------+")
        print("|        1.Crear un usuario.                                            |")
        print("|        2.Cambiar permisos.                                            |")
        print("|        3.Obtener los resultados de un sensor.                         |")
        print("|        4.Actualizar los resultados de un sensor.                      |")
        print("|        0...SALIR...                                                   |")
        print("+-----------------------------------------------------------------------+")
        print('\033[0;m' + "\n")
        
        opcion = -1
        while(opcion >4 or opcion < 0):
            opcion  = int(input("\tIntroduce la opcion a la que desees acceder:"))
            if(opcion >4 or opcion < 0):
                print("ERROR --> Porfavor introduce una opción de entre las que se encuentren disponibles.")

        return opcion
