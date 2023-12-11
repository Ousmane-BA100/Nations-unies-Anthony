from datetime import datetime


class GoodsFlow :
    def __init__(self):
        self.__goodsFlowId: int = None
        self.__countryFrom: str = ""
        self.__countryTo: str = ""
        self.__value: int = None
        self.__year: int = None
        self.__description: str = ""
        self.__status: str = ""

    def setGoodsFlowId(self, goodsflowId : int) -> None:
        '''
        la méthode qui permet d'insérer une valeur dans l'attribut brandId
        :param brandId: l'identifiant de la marque
        :return: rien
        '''
        self.__goodsFlow_Id = goodsflowId
    def getGoodsFlowId(self) -> int:
        '''
        cette méthode permet de retourner l'identifiant d'une marque
        :return: l'id d'une marque
        '''
        return self.__goodsFlow_Id

    def setCountryFrom(self, countryFrom: str) -> None:
        '''
        la méthode qui permet d'insérer une valeur dans l'attribut brandId
        :param brandId: l'identifiant de la marque
        :return: rien
        '''
        self.__countryFrom = countryFrom

    def getCountryFrom(self) -> str:
        '''
        cette méthode permet de retourner l'identifiant d'une marque
        :return: l'id d'une marque
        '''
        return self.__countryFrom

    def setCountryTo(self, countryTo: str) -> None:
        '''
        la méthode qui permet d'insérer une valeur dans l'attribut brandId
        :param brandId: l'identifiant de la marque
        :return: rien
        '''
        self.__countryTo = countryTo

    def getCountryTo(self) -> str:
        '''
        cette méthode permet de retourner l'identifiant d'une marque
        :return: l'id d'une marque
        '''
        return self.__countryTo

    def setValue(self, value: int) -> None:
        '''
        la méthode qui permet d'insérer une valeur dans l'attribut brandId
        :param brandId: l'identifiant de la marque
        :return: rien
        '''
        self.__value = value

    def getValue(self) -> int:
        '''
        cette méthode permet de retourner l'identifiant d'une marque
        :return: l'id d'une marque
        '''
        return self.__value

    def setYear(self, year: int) -> None:
        '''
        la méthode qui permet d'insérer une valeur dans l'attribut brandId
        :param brandId: l'identifiant de la marque
        :return: rien
        '''
        self.__year = year

    def getYear(self) -> int:
        '''
        cette méthode permet de retourner l'identifiant d'une marque
        :return: l'id d'une marque
        '''
        return self.__year

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


