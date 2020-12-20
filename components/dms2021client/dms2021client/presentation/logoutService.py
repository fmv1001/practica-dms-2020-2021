from dms2021client.data.rest import AuthService

class Exit():

    __session_id: str
    __auth_service: AuthService

    def __init__(self, session_id: str, auth_service: AuthService):
        self.__session_id = session_id
        self.__auth_service = auth_service

    def exitPagina(self):
        try:
            self.__auth_service.logout(self.__session_id)
            print('Logged out successfully')
            return -1
        except Exception as ex:
            print(ex)
        
        return 0