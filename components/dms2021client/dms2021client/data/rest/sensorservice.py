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
        """ Proporciona la salidaa de un sensor indicado.
        ---
        Returns: 
            Tipo de sensor.
        """

        connection: HTTPConnection = self.__get_connection()
        connection.request('GET', '/consultarsensor/' + sensor_type)
        response: HTTPResponse = connection.getresponse()

        if response.status == 200:
            print("\t\t·Respuesta del sensor:")
            json_response = response.read()
            sesnor_dict = json.loads(json_response)
            print("\t\t",sesnor_dict)
        else:
            print("Hay algún error en el sensorrest, error: ", response.status)
            print("Respuesta del sensor errado:")
            json_response = response.read()
            sesnor_dict = json.loads(json_response)
            print("\t\t",sesnor_dict)
        return 
    
    def actualizar_sensor(self, sensor_type: str):
        """ Actualiza el sensor indicado.
        ---
        Returns: 
            Tipo de sensor.
        """
        connection: HTTPConnection = self.__get_connection()
        connection.request('POST', '/actualizarsensor/' + sensor_type)
        response: HTTPResponse = connection.getresponse()
        
        if response.status == 200:
            print("\t\t·Respuesta del sensor:")
            json_response = response.read()
            sesnor_dict = json.loads(json_response)
            print("\t\t",sesnor_dict)
        else:
            print("Hay algún error en el sensorrest, error: ", response.status)
            print("Respuesta del sensor errado:")
            json_response = response.read()
            sesnor_dict = json.loads(json_response)
            print("\t\t",sesnor_dict)
        return
