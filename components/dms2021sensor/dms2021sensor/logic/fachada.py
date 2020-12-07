
from sensor1 import SensorMem
from sensor2 import SensorSwap
from sensor3 import SensorArchivoX

sensor1 = SensorMem()
sensor2 = SensorSwap()
sensor3 = SensorArchivoX("/home/fran/Escritorio")
#sensor 4 -> df -h | grep sda1
print(sensor1)
print(sensor2)
print(sensor3)


