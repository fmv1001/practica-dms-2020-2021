class sensorSTR():
    def __init__(self, sesnor1_dict:dict):
        self.__dict = sesnor1_dict
        return
    
    def mostrarSesnor(self):

        for i in self.__dict.keys():
            if i == "RAM":
                valor = int(float(self.__dict[i]))
                print("\t\t\t- La memoria RAM del sistema esta ocupada un " + str(valor) + "%")
                if valor <= 70:
                    print("\t\t\t  RAM valor normal ")
                else:
                    print("\t\t\t  El porcentaje de RAM usada es demasiado alto, se pueden producir errores en el sistema")
            elif i == "SWAP":
                valor = int(float(self.__dict[i]))
                print("\t\t\t- La memoria SWAP del sistema esta ocupada un " + str(valor) + "%")
                if valor <= 70:
                    print("\t\t\t  SWAP valor normal ")
                else:
                    print("\t\t\t  El porcentaje de SWAP usada es demasiado alto, se pueden producir errores en el sistema")
            elif i == "DISK":
                valor = int(float(self.__dict[i]))
                print("\t\t\t- La memoria del disco del sistema esta ocupada un " + str(valor) + "%")
                if valor <= 85:
                    print("\t\t\t  Disco valor normal ")
                else:
                    print("\t\t\t  El porcentaje de memoria usada en el disco es demasiado alto, se pueden producir errores en el sistema")
            elif i == "CPU":
                valor = int(float(self.__dict[i]))
                print("\t\t\t- El porcentaje de uso de la CPU es " + str(valor) + "%")
                if valor <= 80:
                    print("\t\t\t  CPU valor normal ")
                else:
                    print("\t\t\t  El porcentaje de CPU es demasiado alto, se pueden producir errores en el sistema")
            elif i == "Ruta":
                print("\t\t\t- La ruta del archivo es " + str(self.__dict[i]))
            elif i == "Exist":
                valor = bool(self.__dict[i])
                if valor == True:
                    print("\t\t\t- El archivo esta en el sistema ")
                else:
                    print("\t\t\t- El archivo no esta en el sistema ")
            elif i == "MEM":
                valor = int(float(self.__dict[i]))
                print("\t\t\t- El archivo ocupa " + str(valor) + " KB")
                if valor <= 10000:
                    print("\t\t\t  Valor normal de ocupacion en KB")
                else:
                    print("\t\t\t  El archivo pesa mucho, ocupa mucha memoria en el disco")
            elif i == "FECHAMOD":
                print("\t\t\t- La fecha de modificacion mas reciente es " + str(self.__dict[i]))
            else:
                print("\t\t\t- Ha habido algun error no detectado")
        
        return