import dao.ProductsDAO
import model.ProductsM
from model.ProductsM import *
from dao.ProductsDAO import *
#from model.ProductsM import *

class Products:

    @staticmethod
    def ajouterProd(prodObj: Products)->int|str:
        """
        Ajouter un produit.
        @param prodObj: Objet produit à ajouter.
        @return: Statut de l'ajout du produit.
        """
        try:

            prodDAO = ProductsDAO()

            addProd: int = prodDAO.insererUn(prodObj)

            if addProd==0:
                return "ERROR"

            return "INSERTION PRODUIT AVEC SUCCES"

        except Exception as e:

            print(f"Erreur_ProductsC.ajouterProd() ::: {e}")

        return None

    @staticmethod
    def modifierProd(prodId, name, price, qty)->int|str:
        """
        Modifier un produit.
        @param prodId: Identifiant du produit à modifier.
        @param name: Nouveau nom du produit.
        @param price: Nouveau prix du produit.
        @param qty: Nouvelle quantité en stock.
        @return: Statut de la modification du produit.
        """
        try:

            prodDAO = ProductsDAO()

            prod = model.ProductsM.Products()

            prod.setPrice(price)
            prod.setStockQuantity(qty)
            prod.setProductName(name)

            modProd: int = prodDAO.modifierUn(prodId, prod)

            if modProd==0:
                return "ERROR"

            return "MISE A JOUR PRODUIT AVEC SUCCES"

        except Exception as e:

            print(f"Erreur_ProductsC.modifierProd() ::: {e}")

        return None


    @staticmethod
    def consulterUnProd(prodName: str)->Products|str:
        """
        Consulter un produit par nom.
        @param prodName: Nom du produit à consulter.
        @return: Informations sur le produit au format JSON.
        """
        try:

            prodDAO = ProductsDAO()

            modProd: model.ProductsM.Products = prodDAO.trouverUn(prodName)

            if modProd==0:
                return "ERROR"

            return "MISE A JOUR PRODUIT AVEC SUCCES"

        except Exception as e:

            print(f"Erreur_ProductsC.modifierProd() ::: {e}")

        return None

    def consulterUnProdbyId(prodId: int)->Products|str:
        """
        Consulter un produit par identifiant.
        @param prodId: Identifiant du produit à consulter.
        @return: Informations sur le produit au format JSON.
        """
        try:

            prodDAO = ProductsDAO()

            modProd: model.ProductsM.Products = prodDAO.trouverUn(prodId)

            if modProd == 0:
                return "ERROR"

            return "MISE A JOUR PRODUIT AVEC SUCCES"

        except Exception as e:

            print(f"Erreur_ProductsC.modifierProd() ::: {e}")

        return None

    @staticmethod
    def consulterCatalogueProd()->list[dict]|str:
        """
        Consulter le catalogue des produits.
        @return: Liste des produits au format JSON.
        """
        try:

            prodDAO = ProductsDAO()

            listProds = prodDAO.catalogueProduits()

            if listProds == None:
                return "ERROR"

            return listProds

        except Exception as e:

            print(f"Erreur_ProductsC.modifierProd() ::: {e}")

        return None

    @staticmethod
    def supprimerProd(prodId)->int|str:
        """
        Supprimer un produit.
        @param prodId: Identifiant du produit à supprimer.
        @return: Statut de la suppression du produit.
        """

        try:

            prodDAO = ProductsDAO()

            delProd: int = prodDAO.supprimerUn(prodId)

            if delProd == 0:
                return "ERROR"

            return "SUPPRESSION PRODUIT AVEC SUCCES"

        except Exception as e:

            print(f'Erreur_ProductC.supprimerProd() ::: {e}')


    @staticmethod
    def filtrerProdByPrice() -> list[Products] | str:
        """
        Filtrer les produits par prix.
        @return: Liste des produits filtrés au format JSON.
        """
        try:

            prodDAO = ProductsDAO()

            listProds: list[model.ProductsM.Products] = prodDAO.sortProductByPrice()

            if listProds == None:
                return "ERROR"

            return listProds

        except Exception as e:

            print(f"Erreur_ProductsC.filtrerProdByPrice() ::: {e}")

        return None

    @staticmethod
    def search_product_by_name(keyword) -> list[Products]|str:
        """
        Rechercher des produits par nom.
        @param keyword: Mot-clé de recherche.
        @return: Liste des produits correspondant à la recherche au format JSON.
        """
        try:

            prodDAO = ProductsDAO()

            listProds: list[model.ProductsM.Products] = prodDAO.searchPleinText(keyword)

            if listProds == None:
                return "ERROR"

            return listProds

        except Exception as e:

            print(f"Erreur_ProductsC.search_product_by_name() ::: {e}")

        return None