""" Sensor abstract class module.
"""

from abc import ABC, abstractmethod
class Sensor(ABC):
    """ Clase responsable de la abstraccion de los sensores
    """

    @abstractmethod
    def actualizarSensor(self):
        """ Actualiza los valores del sensor
        """

        pass

    @abstractmethod
    def cambiar_reglas(self, regla):
        """ Monitoriza las reglas del sensor1
        ---
        Parameters:
            - regla: regla que se desea cambiar
        """

        pass

    @abstractmethod
    def obtenerSensor(self):
        """ Devuelve el diccionario con los valores del sensor
        ---
        Returns:
            Diccionario con los valores del sensor
        """
        
        pass
