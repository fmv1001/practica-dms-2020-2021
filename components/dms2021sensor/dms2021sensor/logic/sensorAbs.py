

from abc import ABC, abstractmethod
class Sensor(ABC):

    @abstractmethod
    def copy(self):
        pass
