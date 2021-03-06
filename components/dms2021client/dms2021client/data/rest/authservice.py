""" AuthService class module.
"""

import json
from urllib.parse import urlencode
from http.client import HTTPConnection, HTTPResponse, HTTPException
from dms2021client.data.rest.exc import InvalidCredentialsError, UnauthorizedError
from dms2021core.data import UserRightName


class AuthService():
    """ REST client to connect to the authentication service.
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
        """ Creates a new connection to the authentication server.
        ---
        Returns:
            The connection object.
        """

        return HTTPConnection(self.__host, self.__port)

    def is_running(self) -> bool:
        """ Tests whether the authentication service is running or not.
        ---
        Returns:
            True if the authentication service could be contacted successfully; false otherwise.
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

    def login(self, username: str, password: str) -> str:
        """ Logs in a user in the authentication server.
        ---
        Parameters:
            - username: The user name string.
            - password: The user password string.
        Returns:
            The session id string.
        Throws:
            - InvalidCredentialsError: If the credentials provided are not correct.
            - HTTPException: On an unhandled 500 error.
        """

        form: str = urlencode({'username': username, 'password': password})
        headers: dict = {
            'Content-type': 'application/x-www-form-urlencoded'
        }
        connection: HTTPConnection = self.__get_connection()
        connection.request('POST', '/sessions', form, headers)
        response: HTTPResponse = connection.getresponse()
        if response.status == 200:
            response_data_json = response.read()
            response_data = json.loads(response_data_json)
            return response_data['session_id']
        if response.status == 401:
            raise InvalidCredentialsError()
        if response.status == 500:
            raise HTTPException('Server error')
        return ''

    def logout(self, session_id: str):
        """ Logs out a user from the authentication server.
        ---
        Parameters:
            - session_id: The session id string.
        Throws:
            - UnauthorizedError: If the provided session is incorrect or closed.
            - HTTPException: On an unhandled 500 error.
        """

        form: str = urlencode({'session_id': session_id})
        headers: dict = {
            'Content-type': 'application/x-www-form-urlencoded'
        }
        connection: HTTPConnection = self.__get_connection()
        connection.request('DELETE', '/sessions', form, headers)
        response: HTTPResponse = connection.getresponse()
        if response.status == 200:
            return

        if response.status == 401:
            raise UnauthorizedError()
        if response.status == 500:
            raise HTTPException('Server error')

    def newUser(self, usernameAdmin: str,username: str, password: str, session_id: str):
        """ Crea un nuevo usurio en el sistema.
        ---
        Parameters:
            - usernameAdmin: Usuario admin que realiza la operacion.
            - username: nombre del nuevo usuario
            - password: contrasena del nuevo usuario
            - session_id: id de la session actual
        Returns:
            Status of the action
        Throws:
            - UnauthorizedError: If the provided session is incorrect or closed.
        """

        form: str = urlencode({'username': username, 'password': password, 'session_id': session_id})
        headers: dict = {
            'Content-type': 'application/x-www-form-urlencoded'
        }
        connection: HTTPConnection = self.__get_connection()
        connection.request('GET', '/users/' + usernameAdmin + '/rights/AdminUsers')
        response: HTTPResponse = connection.getresponse()
        if response.status == 200:
            connection = self.__get_connection()
            connection.request('POST', '/users',form, headers)
            response = connection.getresponse()
            if response.status == 200:
                return response.status
            else:
                print("Usuario no creado con éxito --> ", response.status)
        elif response.status == 401:
            raise UnauthorizedError()
        else:
            print("ERROR: ....", response.status)
            return response.status

        return response.status

    def dar_quitar_permisos(self, usernameAdmin: str, usernameChanges: str, rightChanges: int, session_id: str, dar_quitar:str):
        """ modifica los permisos de un usurio en el sistema.
        ---
        Parameters:
            - usernameAdmin: Usuario admin que realiza la operacion.
            - username: nombre del usuario a modificar permisos
            - password: contrasena del usuario a modificar permisos
            - session_id: id de la session actual
        Returns:
            Status of the action
        Throws:
            - UnauthorizedError: If the provided session is incorrect or closed.
            - HTTPException: On an unhandled 500 error.
        """

        form: str = urlencode({'session_id': session_id})
        headers: dict = {
            'Content-type': 'application/x-www-form-urlencoded'
        }
        right_change:str = ''
        if rightChanges == 1:
            right_change = 'AdminUsers'
        elif rightChanges == 2:
            right_change = 'AdminRights'
        elif rightChanges == 3:
            right_change = 'AdminSensors'
        elif rightChanges == 4:
            right_change = 'AdminRules'
        elif rightChanges == 5:
            right_change = 'ViewReports'

        connection: HTTPConnection = self.__get_connection()
        connection.request('GET', '/users/' + usernameAdmin + '/rights/AdminRights')
        response: HTTPResponse = connection.getresponse()
        if response.status == 200:
            connection.request(dar_quitar, '/users/' + usernameChanges + '/rights/' + right_change, form, headers)
            response = connection.getresponse()
            if response.status == 200:
                return response.status
            elif response.status == 500:
                raise HTTPException('Server error')
            else:
                print("ERROR, no se de el permiso correctamente por el error --> ", response.status)
                return response.status
        elif response.status == 401:
            raise UnauthorizedError()
        else:
            print("Error....", response.status)
            return response.status

    def has_right(self, usernameAdmin: str, right: str):
        """ Comprobamos que el usuario tenga derechos.
        ---
        Parameters:
            - usernameAdmin: Usuario admin que realiza la operacion.
        Returns:
            Status of the action
        Throws:
            - UnauthorizedError: If the provided session is incorrect or closed.
        """

        connection: HTTPConnection = self.__get_connection()
        connection.request('GET', '/users/' + usernameAdmin + '/rights/' + right)
        response: HTTPResponse = connection.getresponse()
        return response.status
