from dao import ModelDAO
from model.BrandsM import  Brands

class BrandsDAO(ModelDAO.modeleDAO):

    def __init__(self):
        '''
        Initialise l'objet BrandsDAO en établissant une connexion à la base de données.
        '''
        params = ModelDAO.modeleDAO.connect_objet
        self.cur = params.cursor()

    def insererUn(self, objIns: Brands) -> int:
        '''
        Insère un objet dans la table Brands.

        :param objIns: L'objet à insérer dans la table.
        :return: Le nombre de lignes affectées.
        '''
        try:
            query = '''INSERT INTO brands (brand_id, brand_name) 
                       VALUES (%s, %s);'''
            self.cur.execute(query, (objIns.getBrandId(), objIns.getBrandName()))
            self.cur.connection.commit() #fin de la transaction
            #le nombre de lignes validé par la dernière opération SQL exécutée.
            return self.cur.rowcount if self.cur.rowcount!=0 else 0
        except Exception as e:
            print(f"Erreur_BrandsDAO.insererUn() ::: {e}")
            #annuler toutes les modifications non validées depuis le dernier appel à commit()
            self.cur.connection.rollback()
        finally:
            self.cur.close()
        # return 0

    def insererToutList(self, objInsList:list[Brands]=[]) -> int:
        '''
        Insère une liste d'objets dans la table Brands.

        :param objInsList: La liste d'objets à insérer.
        :return: Le nombre de lignes affectées.
        '''
        pass

    def trouverUn(self, cleTrouv) -> Brands:
        '''
        Trouve un objet dans la table Brands par clé.

        :param cleTrouv: La clé de recherche.
        :return: L'objet trouvé.
        '''
        try:
            query = '''SELECT * FROM brands WHERE brand_id = %s;'''
            self.cur.execute(query, (cleTrouv,))
            res = self.cur.fetchone()

            if res:

                b = Brands()

                b.setBrandId(res[0])
                b.setBrandName(res[1])

                return b
            else:
                return None
        except Exception as e:
            print(f"Erreur_BrandsDAO.trouverUn() ::: {e}")
        finally:
            self.cur.close()
        # return None

    def trouverTout(self) -> list[Brands]:
        '''
        Récupère tous les enregistrements de la table Brands.

        :return: Une liste d'objets Brands.
        '''
        try:
            query = '''SELECT * FROM brands;'''
            self.cur.execute(query)
            res = self.cur.fetchall()

            liste_b = [] # [Brands(brand_id=row[0], brand_name=row[1]) for row in res] if res else None

            if len(res)>0:

                for r in res:
                    b = Brands()

                    b.setBrandId(r[0])
                    b.setBrandName(r[1])

                    liste_b.append(b)

                return liste_b

            else:

                return None
        except Exception as e:
            print(f"Erreur_CustomersDAO.trouverTout() ::: {e}")
        finally:
            self.cur.close()
        # return None

    def trouverToutParUn(self, cleTrouv) -> list[Brands]:
        '''
        Récupère tous les enregistrements de la table Brands par une clé spécifique.

        :param cleTrouv: La clé de recherche.
        :return: Une liste d'objets Brands.
        '''
        try:
            query = '''SELECT * FROM brands WHERE brand_name = %s;'''
            self.cur.execute(query, (cleTrouv,))
            res = self.cur.fetchall()

            liste_b = []

            if len(res)>0:

                for r in res:
                    b = Brands()

                    b.setBrandId(r[0])
                    b.setBrandName(r[1])

                    liste_b.append(b)

                return liste_b

            else:

                return None

        except Exception as e:
            print(f"Erreur_BrandsDAO.trouverToutParUn() ::: {e}")
        # finally:
        #     self.cur.close()
        # return None

    def trouverToutParUnLike(self, val) -> list[Brands]:
        '''
        Récupère tous les enregistrements de la table Brands par une clé similaire.

        :param cleTrouv: La clé de recherche similaire.
        :return: Une liste d'objets Brands.
        '''
        try:
            query = '''SELECT * FROM brands WHERE brand_name LIKE %s;'''
            self.cur.execute(query, (val,))
            res = self.cur.fetchall()

            liste_b = []

            if len(res)>0:

                for r in res:
                    b = Brands()

                    b.setBrandId(r[0])
                    b.setBrandName(r[1])

                    liste_b.append(b)

                return liste_b

            else:

                return None

        except Exception as e:
            print(f"Erreur_BrandsDAO.trouverToutParUn() ::: {e}")
        # finally:
        #     self.cur.close()
        # return None

    def modifierUn(self, cleAnc, objModif: Brands) -> int:
        '''
        Modifie un enregistrement dans la table Brands.

        :param cleAnc: La clé de l'enregistrement à modifier.
        :param objModif: Les nouvelles données à mettre à jour.
        :return: Le nombre de lignes affectées.
        '''
        try:
            query = '''UPDATE brands SET brand_name = %s, WHERE brand_id = %s;'''
            self.cur.execute(query, (objModif.getBrandName(), cleAnc))
            self.cur.connection.commit()
            return self.cur.rowcount if self.cur.rowcount!=0 else 0
        except Exception as e:
            print(f"Erreur_BrandsDAO.modifierUn() ::: {e}")
            self.cur.connection.rollback()
        finally:
            self.cur.close()

    def supprimerUn(self, cleSup) -> int:
        '''
        Supprime un enregistrement de la table Brands.

        :param cleSup: La clé de l'enregistrement à supprimer.
        :return: Le nombre de lignes affectées.
        '''
        try:
            query = f'''DELETE FROM brands WHERE brand_id = %s;'''
            self.cur.execute(query, (cleSup,))
            self.cur.connection.commit()
            return self.cur.rowcount if self.cur.rowcount!=0 else 0
        except Exception as e:
            print(f"Erreur_BrandsDAO.supprimerUn() ::: {e}")
            self.cur.connection.rollback()
        finally:
            self.cur.close()

    def depensesMoyennes(self) -> float:
        '''
        Calcule la moyenne des dépenses effectuées par le client.

        :return: La moyenne des dépenses.
        '''
        pass

    def filtrerCmdByStatus(self) -> list:
        '''
        Filtrage des commandes par statut.

        :return: Une liste de commandes filtrée.
        '''
        pass

    def sortProductByPrice(self) -> list:
        '''
        Trie les produits par prix.

        :return: Une liste de produits triés.
        '''
        pass

    def searchPleinText(self) -> list:
        '''
        Effectue une recherche plein texte.

        :return: Une liste de résultats de recherche.
        '''
        pass

    def creerUser(self, pwd, usr) -> object:
        '''
        Crée un nouvel utilisateur.

        :param pwd: Le mot de passe de l'utilisateur.
        :param usr: Le nom d'utilisateur.
        :return: L'objet utilisateur créé.
        '''
        pass

    def creerRole(self, role) -> int:
        '''
        Crée un nouveau rôle.

        :param role: Le rôle à créer.
        :return: Le nombre de lignes affectées.
        '''
        pass

    def attribuerRole(self, usr, role) -> int:
        '''
        Attribue un rôle à un utilisateur.

        :param usr: L'utilisateur auquel attribuer le rôle.
        :param role: Le rôle à attribuer.
        :return: Le nombre de lignes affectées.
        '''
        pass


#if __name__ == "__main__":
#    c = BrandsDAO()
    #
#    res = c.trouverTout()
    #
#    print(res)
