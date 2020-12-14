

from abc import ABC, abstractmethod
class Sensor(ABC):

    @abstractmethod
    def __monitorizar(self):
        pass

    @abstractmethod
    def copy(self):
        pass
