import os
class MenuPrincipal():

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
        print("|        5.Cambiar las reglas de un sensor.                             |")
        print("|        6...LogOut...                                                  |")
        print("|        0...LogOut and exit...                                         |")
        print("+-----------------------------------------------------------------------+")
        print('\033[0;m' + "\n")

        opcion = -1
        while(opcion >6 or opcion < 0):
            opcion  = int(input('\033[1;37m' + "\tIntroduce la opcion a la que desees acceder: " + '\033[0;m'))
            if(opcion >6 or opcion < 0):
                print("\x1b[1;33m" + "ERROR --> " + '\033[0;m' + "Porfavor introduce una opción de entre las que se encuentren disponibles.")

        return opcion
