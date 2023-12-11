from datetime import datetime


class Treaty :
    def __init__(self):
        self.__treatyId: int = None
        self.__name: str = ""
        self.__date: datetime = ""
        self.__participants: str = ""
        self.__description: str = ""
        self.__status: str = ""

    def setTreatyId(self, treatyId : int) -> None:
        '''
        la méthode qui permet d'insérer une valeur dans l'attribut brandId
        :param brandId: l'identifiant de la marque
        :return: rien
        '''
        self.__treaty_id = treatyId
    def getTreatyId(self) -> int:
        '''
        cette méthode permet de retourner l'identifiant d'une marque
        :return: l'id d'une marque
        '''
        return self.__treaty_id

    def setName(self, name : int) -> None:
        '''
        la méthode qui permet d'insérer une valeur dans l'attribut brandId
        :param brandId: l'identifiant de la marque
        :return: rien
        '''
        self.__name = name
    def getName(self) -> str:
        '''
        cette méthode permet de retourner l'identifiant d'une marque
        :return: l'id d'une marque
        '''
        return self.__name

    def setDate(self, date : datetime) -> None:
        '''
        la méthode qui permet d'insérer une valeur dans l'attribut brandId
        :param brandId: l'identifiant de la marque
        :return: rien
        '''
        self.__date = date
    def getDate(self) -> datetime:
        '''
        cette méthode permet de retourner l'identifiant d'une marque
        :return: l'id d'une marque
        '''
        return self.__date

    def setParticipants(self, participants : str) -> None:
        '''
        la méthode qui permet d'insérer une valeur dans l'attribut brandId
        :param brandId: l'identifiant de la marque
        :return: rien
        '''
        self.__participants = participants
    def getParticipants(self) -> str:
        '''
        cette méthode permet de retourner l'identifiant d'une marque
        :return: l'id d'une marque
        '''
        return self.__participants

    def setDescription(self, description : str) -> None:
        '''
        la méthode qui permet d'insérer une valeur dans l'attribut brandId
        :param brandId: l'identifiant de la marque
        :return: rien
        '''
        self.__description = description
    def getDescription(self) -> str:
        '''
        cette méthode permet de retourner l'identifiant d'une marque
        :return: l'id d'une marque
        '''
        return self.__description

    def setStatus(self, status : str) -> None:
        '''
        la méthode qui permet d'insérer une valeur dans l'attribut brandId
        :param brandId: l'identifiant de la marque
        :return: rien
        '''
        self.__status = status
    def getStatus(self) -> str:
        '''
        cette méthode permet de retourner l'identifiant d'une marque
        :return: l'id d'une marque
        '''
        return self.__status