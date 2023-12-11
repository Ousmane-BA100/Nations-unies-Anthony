from dao.CustomersDAO import *
from model import ProductsM, OrdersM, OrderDetailsM, CustomersM, BodyPartsM, GendersM

class Customers:

    @staticmethod
    def visualiserCustomers()-> str | CustomersM.Customers:
        '''
        Visualise tous les clients.
        @return: Liste de clients ou message d'erreur.
        '''
        try:

            cDAO = CustomersDAO()

            c: list[CustomersM.Customers]|str = cDAO.trouverTout()

            if c==None :
                return "ERROR"

            return c

        except Exception as e:
            print(f'Erreur_CustomersC.visualiserCustomers() ::: {e}')

        return None

    @staticmethod
    def visualiserUnCustomers(idC):
        '''
        Visualise un client spécifique.
        @param idC: ID du client.
        @return: Client spécifique ou message d'erreur.
        '''
        try:

            cDAO = CustomersDAO()

            c: CustomersM.Customers = cDAO.trouverUn(idC)

            if c == None :
                return "ERROR"

            return c

        except Exception as e:
            print(f'Erreur_CustomersC.visualiserUneBrands() ::: {e}')

        return None


    @staticmethod
    def ajouterUnCustomer(idC, nameC, email, phone_number):
        '''
        Ajoute un client.
        @param idC: ID du client.
        @param nameC: Nom du client.
        @param email: Adresse e-mail du client.
        @param phone_number: Numéro de téléphone du client.
        @return: Statut de l'ajout du client.
        '''
        try:

            cDAO = CustomersDAO()

            objC = CustomersM.Customers()

            objC.setCustomerID(idC)
            objC.setCustomerName(nameC)
            objC.setEmail(email)
            objC.setPhoneNumber(phone_number)

            c: int = cDAO.insererUn(objC)

            if c==0 :
                return "ERROR"

            return "AJOUT Customer AVEC SUCCES"

        except Exception as e:
            print(f'Erreur_CustomersC.ajouterUnCustomer() ::: {e}')

        return None

    @staticmethod
    def modifierUnCstomer(idC, nameC, email, phone_number):
        '''
        Modifie un client.
        @param idC: ID du client.
        @param nameC: Nouveau nom du client.
        @param email: Nouvelle adresse e-mail du client.
        @param phone_number: Nouveau numéro de téléphone du client.
        @return: Statut de la modification du client.
        '''
        try:

            cDAO = CustomersDAO()

            objC = CustomersM.Customers()

            objC.setCustomerID(idC)
            objC.setCustomerName(nameC)
            objC.setEmail(email)
            objC.setPhoneNumber(phone_number)

            c: int = cDAO.modifierUn(idC, objC)

            if c==0 :
                return "ERROR"

            return "MODIFICATION DE Customer AVEC SUCCES"

        except Exception as e:
            print(f'Erreur_CustomersC.modifierUnCstomer() ::: {e}')

        return None

    @staticmethod
    def supprimerUnCustomer(idC):
        '''
        Supprime un client.
        @param idC: ID du client.
        @return: Statut de la suppression du client.
        '''
        try:

            cDAO = CustomersDAO()

            c: int = cDAO.supprimerUn(idC)

            if c==0 :
                return "ERROR"

            return "SUPPRESSION Customers AVEC SUCCES"

        except Exception as e:
            print(f'Erreur_CustomersC.supprimerUnCustomer() ::: {e}')

        return None