class Country :
    def __init__(self):
        self.__CountryId: int = None
        self.__Country_name: str=""
        self.__capital: str=""
        self.__population: int = None
        self.__area: int = None

    def setCountryId(self, countryId : int) -> None:
        '''
        la méthode qui permet d'insérer une valeur dans l'attribut brandId
        :param brandId: l'identifiant de la marque
        :return: rien
        '''
        self.__country_id = countryId
    def getCountryId(self) -> int:
        '''
        cette méthode permet de retourner l'identifiant d'une marque
        :return: l'id d'une marque
        '''
        return self.__country_id


    def setCountry_name(self, country_name : str) -> None:
        '''
        la méthode qui permet d'insérer une valeur dans l'attribut brandId
        :param brandId: l'identifiant de la marque
        :return: rien
        '''
        self.__country_name = country_name
    def getCountry_name(self) -> str:
        '''
        cette méthode permet de retourner l'identifiant d'une marque
        :return: l'id d'une marque
        '''
        return self.__country_name


    def setCapital(self,  capital : str) -> None:
        '''
        la méthode qui permet d'insérer une valeur dans l'attribut brandId
        :param brandId: l'identifiant de la marque
        :return: rien
        '''
        self.__capital = capital
    def getCapital(self) -> str:
        '''
        cette méthode permet de retourner l'identifiant d'une marque
        :return: l'id d'une marque
        '''
        return self.__capital

    def setPopulation(self, population : int) -> None:
        '''
        la méthode qui permet d'insérer une valeur dans l'attribut brandId
        :param brandId: l'identifiant de la marque
        :return: rien
        '''
        self.__population = population
    def getPopulation(self) -> int:
        '''
        cette méthode permet de retourner l'identifiant d'une marque
        :return: l'id d'une marque
        '''
        return self.__population

    def setArea(self, area : int) -> None:
        '''
        la méthode qui permet d'insérer une valeur dans l'attribut brandId
        :param brandId: l'identifiant de la marque
        :return: rien
        '''
        self.__area = area
    def getArea(self) -> int:
        '''
        cette méthode permet de retourner l'identifiant d'une marque
        :return: l'id d'une marque
        '''
        return self.__area