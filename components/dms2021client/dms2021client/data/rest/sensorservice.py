""" AuthService class module.
"""

import json
from urllib.parse import urlencode
from http.client import HTTPConnection, HTTPResponse, HTTPException
from dms2021client.data.rest.exc import InvalidCredentialsError, UnauthorizedError


class SensorService():
    """ REST client to connect to the sensor service.
    """

    def __init__(self, host: str, port: int):
        """ Constructor method.

        Initializes the client.
        ---
        Parameters:
            - host: The authentication service host string.
            - port: The authentication service port number.
        """
        
        self.__host: str = host
        self.__port: int = port

    def __get_connection(self) -> HTTPConnection:
        """ Creates a new connection to the sensor server.
        ---
        Returns:
            The connection object.
        """
        return HTTPConnection(self.__host, self.__port)

    def is_running(self) -> bool:
        """ Tests whether the authentication service is running or not.
        ---
        Returns:
            True if the sensor service could be contacted successfully; false otherwise.
        """
        try:
            connection: HTTPConnection = self.__get_connection()
            connection.request('GET', '/')
            response: HTTPResponse = connection.getresponse()
            if response.status == 200:
                return True
            return False
        except HTTPException:
            return False
        except ConnectionRefusedError:
            return False

    def create_sensor(self, sensor_type: str):

        connection: HTTPConnection = self.__get_connection()
        print("VOY A ENTRAR")
        connection.request('GET', '/consultarsensor/' + sensor_type)
        response: HTTPResponse = connection.getresponse()
        if response.status == 200:
            print("MUY BIEN!!!")
            print("Respuesta del sensor:")
            print("\t",response.read())
        else:
            print("Hay algún error en el sensorrest, error: ", response.status)
            print("Respuesta del sensor errado:")
            print("\t",response.read())
    
    def actualizar_sensor(self, sensor_type: str):

        connection: HTTPConnection = self.__get_connection()
        print("VOY A ENTRAR")
        connection.request('POST', '/actualizarsensor/' + sensor_type)
        response: HTTPResponse = connection.getresponse()
        if response.status == 200:
            print("MUY BIEN actualizado con exito!!!")
            print("Respuesta del sensor:")
            print("\t",response.read())

        else:
            print("Hay algún error en el sensorrest, error: ", response.status)
            print("Respuesta del sensor errado:")
            print("\t",response.read())
