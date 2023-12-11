from dao import ModelDAO

class sysadmin(ModelDAO.modeleDAO):

    def __init__(self):
        '''
        Initialise l'objet sysadmin en établissant une connexion à la base de données.
        '''
        params = ModelDAO.modeleDAO.connect_objet
        self.cur = params.cursor()

    def insererUn(self, objIns) -> int:
        pass

    def insererToutList(self, objInsList) -> int:
        pass

    def trouverUn(self, cleTrouv) -> object:
        pass

    def trouverTout(self) -> list:
        pass

    def trouverToutParUn(self, cleTrouv) -> list:
        pass

    def trouverToutParUnLike(self, cleTrouv) -> list:
        pass

    def modifierUn(self, cleAnc, objModif) -> int:
        pass

    def supprimerUn(self, cleSup) -> int:
        pass

    def valeurImportation_Moyennes(self) -> float:
        pass

    def valeurExportation_Moyennes(self) -> float:
        pass

    def filtrerTreatyByStatus(self) -> list:
        pass

    def sortProductByValue(self) -> list:
        pass

    def searchPleinText(self) -> list:
        pass

    def creerUser(self, pwd:str, usr:str) -> int:
        '''
        Crée un nouvel utilisateur dans la base de données.

        :param usr: Le nom d'utilisateur.
        :param pwd: Le mot de passe de l'utilisateur.
        :return: Le nombre de lignes affectées.
        '''
        try:
            query = f'''CREATE USER {usr} WITH PASSWORD '{pwd}';''' #f'''CREATE USER {usr} WITH PASSWORD MD5('{pwd}');''' #CREATE EXTENSION IF NOT EXISTS pgcrypto;
            self.cur.execute(query)
            self.cur.connection.commit()
            print(self.cur.rowcount)
            return self.cur.rowcount if self.cur.rowcount != 0 else 0
        except Exception as e:
            print(f"Erreur_SysAdminDAO.creerUser() ::: {e}")
            self.cur.connection.rollback()
        finally:
            self.cur.close()

    def creerRole(self, role) -> int:
        '''
        Crée un nouveau rôle dans la base de données.

        :param role: Le nom du rôle à créer.
        :return: Le nombre de lignes affectées.
        '''
        try:
            query = f'''CREATE ROLE {role};'''
            self.cur.execute(query)
            self.cur.connection.commit()
            return self.cur.rowcount if self.cur.rowcount != 0 else 0
        except Exception as e:
            print(f"Erreur_SysAdminDAO.creerRole() ::: {e}")
            self.cur.connection.rollback()
        finally:
            self.cur.close()

    def attribuerPriviliege(self, privileges:str, tables:str, role:str) -> int:
        '''
        Attribue des privilèges à un rôle.

        :param usr: L'utilisateur auquel attribuer le rôle.
        :param role: Le rôle à attribuer.
        :return: Le nombre de lignes affectées.
        '''
        try:
            query = f'''GRANT {privileges} ON {tables} TO {role};'''
            self.cur.execute(query)
            self.cur.connection.commit()
            return self.cur.rowcount if self.cur.rowcount != 0 else 0
        except Exception as e:
            print(f"Erreur_SysAdminDAO.attribuerRole() ::: {e}")
            self.cur.connection.rollback()
        finally:
            self.cur.close()

    def attribuerRole(self, usr, roles) -> int:
        '''
        Attribue un rôle à un utilisateur.

        :param usr: L'utilisateur auquel attribuer le rôle.
        :param role: Le rôle à attribuer.
        :return: Le nombre de lignes affectées.
        '''
        try:
            query = f'''GRANT {roles} TO {usr};'''
            self.cur.execute(query)
            self.cur.connection.commit()
            return self.cur.rowcount if self.cur.rowcount != 0 else 0
        except Exception as e:
            print(f"Erreur_SysAdminDAO.attribuerRole() ::: {e}")
            self.cur.connection.rollback()
        finally:
            self.cur.close()