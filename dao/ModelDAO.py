from abc import ABC, abstractmethod
from dao.ConnexionDAO import ConnexionBD

class modeleDAO(ABC):

    connect_objet = ConnexionBD().getConnexion()

    ### CRUD

    # INSERT

    @abstractmethod
    def insererUn(self, objIns)->int:
        pass

    @abstractmethod
    def insererToutList(self, objInsList)->int:
        pass

    # SELECT

    @abstractmethod
    def trouverUn(self, cleTrouv)->object:
        pass

    @abstractmethod
    def trouverTout(self)->list:
        pass

    @abstractmethod
    def trouverToutParUn(self, cleTrouv)->list:
        pass

    @abstractmethod
    def trouverToutParUnLike(self, cleTrouv)->list:
        pass

    # UPDATE

    @abstractmethod
    def modifierUn(self, cleAnc, objModif)->int:
        pass

    # DELETE

    @abstractmethod
    def supprimerUn(self, cleSup)->int:
        pass

    # Les différentes questions que le user "nations unies" peut se poser ?
    # 1. La moyenne en valeur d'importation et aussi d'exportation qu'un pays fait sur tous les produits confondus
    # 2. CASE WHEN : filtrer par statut des traités
    # 3. RANK : classer les pays qui exportent/importent plus par valeur croissant
    # 4. @@ : faire une recherche plein texte

    ###############################################################################"
    # SEANCE 4/5 :
    # 1.    La moyenne des dépenses effectuées par le client (PL/SQL)
    # 2.    CASE WHEN : filtrer par statut
    # 3.    RANK : classer les produits par prix croissant
    # 4.    @@ : faire une recherche plein texte

    @abstractmethod
    def valeurImportation_Moyennes(self)->float:
        pass

    @abstractmethod
    def valeurExportation_Moyennes(self) -> float:
        pass

    @abstractmethod
    def filtrerTreatyByStatus(self)->list: #La colonne status de la table treaty
        pass

    @abstractmethod
    def sortProductByValue(self)->list:
        pass

    @abstractmethod
    def searchPleinText(self)->list:
        pass

    # SEANCE 6 :
    # 1.    User/Rôles
    # 2.    MD5 password
    # 3.    Indexation
    # 4.    Enum/DATE_TRUNC

    @abstractmethod
    def creerUser(self, pwd, usr)->object:
        pass

    @abstractmethod
    def creerRole(self, role)->int:
        pass

    @abstractmethod
    def attribuerRole(self, usr,role)->int:
        pass
