
class LoginApp():

    def __init__(self, auth_service, username, password):
        self.__auth_service = auth_service
        self.__username = username
        self.__password = password
        return
    
    def login(self):
        """ Metodo que permite al usuario logearse. """

        session_id: str = self.__auth_service.login(self.__username, self.__password)
            
        return session_id