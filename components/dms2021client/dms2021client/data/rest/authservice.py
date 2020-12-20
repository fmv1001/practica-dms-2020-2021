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

    def newUser(self,username: str, password: str, session_id: str):
        form: str = urlencode({'username': username, 'password': password, 'session_id': session_id})
        headers: dict = {
            'Content-type': 'application/x-www-form-urlencoded'
        }

        connection: HTTPConnection = self.__get_connection()
        connection.request('POST', '/users',form, headers)
        response: HTTPResponse = connection.getresponse()
        if response.status == 200:
            print("MUY BIEN SE HA CREADO!!!")
        else:
            print("VAYA POR DIOS....", response.status)

        return

    def mod_permisos(self, usernameAdmin: str, usernameChanges: str, rightChanges: int):
        form: str = urlencode({'session_id': session_id})
        headers: dict = {
            'Content-type': 'application/x-www-form-urlencoded'
        }

        right_change:str
        if rightChanges == 1:
            right_change = UserRightName.AdminUsers
        elif rightChanges == 2:
            right_change = UserRightName.AdminRights
        elif rightChanges == 3:
            right_change = UserRightName.AdminSensors
        elif rightChanges == 4:
            right_change = UserRightName.AdminRules
        elif rightChanges == 5:
            right_change = UserRightName.ViewReports
        
        connection: HTTPConnection = self.__get_connection()
        connection.request('GET', '/users/' + usernameAdmin + '/rights/'+ UserRightName.AdminRights)
        response: HTTPResponse = connection.getresponse()
        if response.status == 200:
            connection.request('POST', '/users/' + usernameChanges + '/rights/' + right_change, form, headers)
            response: HTTPResponse = connection.getresponse()
            if response.status == 200:
                print("CAMBIO con exito!!")
            elif response.status == 500:
                raise HTTPException('Server error')
            else:
                print("ERROR, no da permiso: ", response.status)
                return
        elif response.status == 401:
            raise UnauthorizedError()
        else:
            print("VAYA POR DIOS....", response.status)
            return

        
