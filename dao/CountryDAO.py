from dao import ModelDAO
from model.CountryM import Country

class CountryDAO(ModelDAO.modeleDAO):

    def __init__(self):
        '''
        Initialise l'objet BrandsDAO en établissant une connexion à la base de données.
        '''
        params = ModelDAO.modeleDAO.connect_objet
        self.cur = params.cursor()

    def insererUn(self, objIns: Country) -> int:
        '''
        Insère un objet dans la table Brands.

        :param objIns: L'objet à insérer dans la table.
        :return: Le nombre de lignes affectées.
        '''
        try:
            query = '''INSERT INTO pays (countryId, country_name, capital, population, area) 
                       VALUES (%s, %s);''',
            self.cur.execute(query, (objIns.get_countryId(), objIns.get_country_name(),
                                     objIns.get_capital(), objIns.get_population(), objIns.get_area()))
            self.cur.connection.commit() #fin de la transaction
            #le nombre de lignes validé par la dernière opération SQL exécutée.
            return self.cur.rowcount if self.cur.rowcount!=0 else 0
        except Exception as e:
            print(f"Erreur_CountryDAO.insererUn() ::: {e}")
            #annuler toutes les modifications non validées depuis le dernier appel à commit()
            self.cur.connection.rollback()
        finally:
            self.cur.close()
        # return 0

    def insererToutList(self, objInsList:list[Country]=[]) -> int:
        '''
        Insère une liste d'objets dans la table Brands.

        :param objInsList: La liste d'objets à insérer.
        :return: Le nombre de lignes affectées.
        '''
        pass

    def trouverUn(self, cleTrouv) -> Country:
        '''
        Trouve un objet dans la table Brands par clé.

        :param cleTrouv: La clé de recherche.
        :return: L'objet trouvé.
        '''
        try:
            query = '''SELECT * FROM Pays WHERE countryId = %s;'''
            self.cur.execute(query, (cleTrouv,))
            res = self.cur.fetchone()

            if res:

                b = Country()

                b.setCountryId(res[0])
                b.setCountry_name(res[1])

                return b
            else:
                return None
        except Exception as e:
            print(f"Erreur_CountryDAO.trouverUn() ::: {e}")
        finally:
            self.cur.close()
        # return None

    def trouverTout(self) -> list[Country]:
        '''
        Récupère tous les enregistrements de la table Brands.

        :return: Une liste d'objets Brands.
        '''
        try:
            query = '''SELECT * FROM country;'''
            self.cur.execute(query)
            res = self.cur.fetchall()

            liste_b = [] # [Brands(brand_id=row[0], brand_name=row[1]) for row in res] if res else None

            if len(res)>0:

                for r in res:
                    b = Country()

                    b.setCountryId(r[0])
                    b.setCountry_name(r[1])

                    liste_b.append(b)

                return liste_b

            else:

                return None
        except Exception as e:
            print(f"Erreur_CountryDAO.trouverTout() ::: {e}")
        finally:
            self.cur.close()
        # return None

    def trouverToutParUn(self, cleTrouv) -> list[Country]:
        '''
        Récupère tous les enregistrements de la table Brands par une clé spécifique.

        :param cleTrouv: La clé de recherche.
        :return: Une liste d'objets Brands.
        '''
        try:
            query = '''SELECT * FROM country WHERE country_name = %s;'''
            self.cur.execute(query, (cleTrouv,))
            res = self.cur.fetchall()

            liste_b = []

            if len(res)>0:

                for r in res:
                    b = Country()

                    b.setCountryId(r[0])
                    b.setCountry_name(r[1])

                    liste_b.append(b)

                return liste_b

            else:

                return None

        except Exception as e:
            print(f"Erreur_CountryDAO.trouverToutParUn() ::: {e}")
        # finally:
        #     self.cur.close()
        # return None

    def trouverToutParUnLike(self, val) -> list[Country]:
        '''
        Récupère tous les enregistrements de la table Brands par une clé similaire.

        :param cleTrouv: La clé de recherche similaire.
        :return: Une liste d'objets Brands.
        '''
        try:
            query = '''SELECT * FROM brands WHERE country_name LIKE %s;'''
            self.cur.execute(query, (val,))
            res = self.cur.fetchall()

            liste_b = []

            if len(res)>0:

                for r in res:
                    b = Country()

                    b.setCountryId(r[0])
                    b.setCountry_name(r[1])

                    liste_b.append(b)

                return liste_b

            else:

                return None

        except Exception as e:
            print(f"Erreur_CountryDAO.trouverToutParUn() ::: {e}")
        # finally:
        #     self.cur.close()
        # return None

    def modifierUn(self, cleAnc, objModif: Country) -> int:
        '''
        Modifie un enregistrement dans la table Brands.

        :param cleAnc: La clé de l'enregistrement à modifier.
        :param objModif: Les nouvelles données à mettre à jour.
        :return: Le nombre de lignes affectées.
        '''
        try:
            query = '''UPDATE brands SET brand_name = %s, WHERE brand_id = %s;'''
            self.cur.execute(query, (objModif.getCountry_name(), cleAnc))
            self.cur.connection.commit()
            return self.cur.rowcount if self.cur.rowcount!=0 else 0
        except Exception as e:
            print(f"Erreur_CountryDAO.modifierUn() ::: {e}")
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
            query = f'''DELETE FROM country WHERE brand_id = %s;'''
            self.cur.execute(query, (cleSup,))
            self.cur.connection.commit()
            return self.cur.rowcount if self.cur.rowcount!=0 else 0
        except Exception as e:
            print(f"Erreur_CountryDAO.supprimerUn() ::: {e}")
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
