class menuDeOpciones():

    def __init__(self):
        return

    def menu(self):
        print("+-----------------------------------------------------------------------+")
        print("| MENU PRINCIPAL -->                                                    |")
        print("+-----------------------------------------------------------------------+")
        print("|        1.Crear un usuario.                                            |")
        print("|        2.Cambiar permisos.                                            |")
        print("|        3.Obtener los resultados de un sensor.                         |")
        print("|        0...SALIR...                                                   |")
        print("+-----------------------------------------------------------------------+")
        print("\n")
        
        opcion = -1
        while(opcion >3 or opcion < 0):
            opcion  = int(input("\tIntroduce la opcion a la que desees acceder:"))
            if(opcion >3 or opcion < 0):
                print("ERROR --> Porfavor introduce una opción de entre las que se encuentren disponibles.")

        return opcion
