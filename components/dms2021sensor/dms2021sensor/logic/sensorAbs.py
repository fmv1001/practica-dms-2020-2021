

from abc import ABC, abstractmethod
class Sensor(ABC):

    @abstractmethod
    def actualizarSensor(self):
        pass

