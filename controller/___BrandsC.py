from dao.BrandsDAO import *
from model import ProductsM, OrdersM, OrderDetailsM, CustomersM, BodyPartsM, GendersM, BrandsM

class Brands:

    @staticmethod
    def visualiserBrands():
        '''
        Visualise toutes les marques.
        @return: Liste de marques.
        '''
        try:

            bDAO = BrandsDAO()

            cs: list[BrandsM.Brands] = bDAO.trouverTout()

            if cs==None :
                return "ERROR"

            return cs

        except Exception as e:
            print(f'Erreur_BrandsC.visualiserBrands() ::: {e}')

        return None

    @staticmethod
    def visualiserUneBrands(idB):
        '''
        Visualise une marque spécifique.
        @param idB: ID de la marque.
        @return: Marque spécifique.
        '''
        try:

            bDAO = BrandsDAO()

            b: BrandsM.Brands = bDAO.trouverUn(idB)

            if b==None :
                return "ERROR"

            return b

        except Exception as e:
            print(f'Erreur_BrandsC.visualiserUneBrands() ::: {e}')

        return None


    @staticmethod
    def ajouterUneBrands(idB, nameB):
        '''
        Ajoute une marque.
        @param idB: ID de la marque.
        @param nameB: Nom de la marque.
        @return: Statut de l'ajout de la marque.
        '''
        try:

            bDAO = BrandsDAO()

            objB = BrandsM.Brands()

            objB.setBrandId(idB)
            objB.setBrandName(nameB)

            bp: int = bDAO.insererUn(objB)

            if bp==0 :
                return "ERROR"

            return "AJOUT Brands AVEC SUCCES"

        except Exception as e:
            print(f'Erreur_BrandsC.ajouterUneBrands() ::: {e}')

        return None

    @staticmethod
    def modifierUnBrands(idB, nameB):
        '''
        Modifie une marque.
        @param idB: ID de la marque.
        @param nameB: Nouveau nom de la marque.
        @return: Statut de la modification de la marque.
        '''
        try:

            bDAO = BrandsDAO()

            objB = BrandsM.Brands()

            objB.setBrandName(nameB)

            b: int = bDAO.modifierUn(idB, objB)

            if b==0 :
                return "ERROR"

            return "MODIFICATION DE Brands AVEC SUCCES"

        except Exception as e:
            print(f'Erreur_BrandsC.modifierUnBrands() ::: {e}')

        return None

    @staticmethod
    def supprimerUneBrands(idB):
        '''
        Supprime une marque.
        @param idB: ID de la marque.
        @return: Statut de la suppression de la marque.
        '''
        try:

            bDAO = BrandsDAO()

            b: int = bDAO.supprimerUn(idB)

            if b==0 :
                return "ERROR"

            return "SUPPRESSION Brands AVEC SUCCES"

        except Exception as e:
            print(f'Erreur_BrandsC.supprimerUneBrands() ::: {e}')

        return None