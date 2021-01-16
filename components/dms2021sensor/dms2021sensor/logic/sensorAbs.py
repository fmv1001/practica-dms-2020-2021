

from abc import ABC, abstractmethod
class Sensor(ABC):

    @abstractmethod
    def actualizarSensor(self):
        pass

    @abstractmethod
    def cambiar_reglas(self, regla):
        pass

    @abstractmethod
    def obtenerSensor(self):
        pass
