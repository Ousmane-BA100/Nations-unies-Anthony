Usage
=====

.. _installation:

utilisation
------------

1. Dans le dossier api > `python mainFlask.py` ou `python mainFast.py`

2. Dans les deux cas, l'adresse est :  `http://127.0.0.1:5000` ou `http://10.188.255.1:5000` ou `http://localhost:5000` ou `http://0.0.0.0:5000`

Fonctionnalités principales pour FlaskAPI
-----------------------------------------


1. **Obtenir la liste des marques :** GET /api/lvmh/sephora/postgresql/getbrands/


2. **Obtenir les produits triés par prix :** GET /api/lvmh/sephora/postgresql/getprodbyprice/


3. **Obtenir le catalogue complet des produits :** GET /api/lvmh/sephora/postgresql/get_catalogue_prod/


4. **Obtenir les dépenses moyennes d'un client :** GET /api/lvmh/sephora/postgresql/depenses_moyenne/<idCustomer>


5. **Obtenir les commandes d'un client par statut :** GET /api/lvmh/sephora/postgresql/cmd_by_status/<idCustomer>/<status>


6. **Rechercher des produits par texte intégral :** GET /api/lvmh/sephora/postgresql/searchPleinText/<keyword>


7. **Passer une commande :** POST /api/lvmh/sephora/postgresql/commander


8. **Créer un nouvel utilisateur :** POST /api/lvmh/sephora/postgresql/create_user


9. **Créer un nouveau rôle :** POST /api/lvmh/sephora/postgresql/create_role


10. **Attribuer des privilèges à un rôle :** POST /api/lvmh/sephora/postgresql/assign_privileges


11. **Attribuer un rôle à un utilisateur :** POST /api/lvmh/sephora/postgresql/assign_role


12. **Annuler une commande :** DELETE /api/lvmh/sephora/postgresql/cancel_order/<order_id>


13. **Générer une facture :** GET /api/lvmh/sephora/postgresql/generate_invoice/<invoice_id>

![img.png](utils/imgFlask.png)

Fonctionnalités principales pour FastAPI
-----------------------------------------


fastAPI donne la posisbilité d'accéder à une documentation générée automatiquement à partir de ce lien :
`http://127.0.0.1:5000/docs`

![img.png](utils/imgFast.png)

