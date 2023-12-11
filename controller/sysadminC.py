from dao.sysadminDAO import *

class SysAdmin:

    @staticmethod
    def creerUnUser(pwd, usr):
        """
        Créer un nouvel utilisateur.
        @param pwd: Mot de passe de l'utilisateur.
        @param usr: Nom d'utilisateur.
        @return: Statut de la création de l'utilisateur.
        """
        try:

            sDAO = sysadmin()

            sys: int = sDAO.creerUser(pwd, usr)
            print("sys:",sys)
            if sys==0 :
                return "ERROR"

            return "CREATION D'UN NOUVEAU USER AVEC SUCCES"

        except Exception as e:
            print(f'Erreur_sysadminC.creerUSER() ::: {e}')

        return None

    @staticmethod
    def creerUnRole(role):
        """
        Créer un nouveau rôle.
        @param role: Nom du rôle à créer.
        @return: Statut de la création du rôle.
        """

        try:

            sDAO = sysadmin()

            sys: int = sDAO.creerRole(role)

            if sys==0 :
                return "ERROR"

            return "CREATION D'UN NOUVEAU USER AVEC SUCCES"

        except Exception as e:
            print(f'Erreur_sysadminC.creerUnRole() ::: {e}')

        return None

    @staticmethod
    def privilege_Role(privileges, tables, roles):
        """
        Attribuer des privilèges à un rôle.
        @param privileges: Liste des privilèges à attribuer.
        @param tables: Liste des tables concernées.
        @param roles: Liste des rôles auxquels attribuer les privilèges.
        @return: Statut de l'attribution des privilèges.
        """
        try:

            sDAO = sysadmin()

            sys: int = sDAO.attribuerPriviliege(privileges, tables, roles)

            if sys==0 :
                return "ERROR"

            return "ATTRIBUTION DE(S) PRIVILEGE(S) A UN ROLE AVEC SUCCES"

        except Exception as e:
            print(f'Erreur_sysadminC.privilege_Role() ::: {e}')

        return None

    @staticmethod
    def attribution_Role(usr, roles):
        """
        Attribuer des rôles à un utilisateur.
        @param usr: Nom de l'utilisateur.
        @param roles: Liste des rôles à attribuer à l'utilisateur.
        @return: Statut de l'attribution des rôles.
        """
        try:

            sDAO = sysadmin()

            sys: int = sDAO.attribuerRole(usr, roles)

            if sys==0 :
                return "ERROR"

            return "ATTRIBUTION DE(S) ROLE(S) A UN USER AVEC SUCCES"

        except Exception as e:
            print(f'Erreur_sysadminC.privilege_Role() ::: {e}')

        return None