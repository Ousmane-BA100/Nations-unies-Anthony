import os
import json
from datetime import datetime
from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from controller import ___ProductsC, ___BrandsC, OrdersC, InvoicesC, sysadminC
from model import ProductsM, BrandsM, OrdersM, InvoicesM

app = FastAPI()

# Configuration CORS pour gérer les accès au web service
origins = ["*"]  # Ajoutez ici vos origines autorisées
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

LOG_FILE_PATH = '/home/keke/DataspellProjects/lvmh_sephora/utils/logs.json'

Privacy_Policy = '''
Confidentialité et sécurité : Nous accordons la priorité à la protection de vos informations et avons mis en place des mesures de sécurité appropriées pour prévenir l'accès, la divulgation ou la modification non autorisés. Seul le personnel autorisé a accès à ces informations, et il est lié par des obligations de confidentialité.

Restrictions d'accès et d'exploration : L'accès non autorisé à notre application, y compris toute tentative d'exploration de son fonctionnement en accédant à la racine de l'API, est strictement interdit. Toute violation de cette politique de confidentialité ou de nos conditions d'utilisation peut entraîner des mesures disciplinaires, y compris la résiliation du compte et, si nécessaire, des poursuites judiciaires.

Conservation des informations : Nous conservons vos informations aussi longtemps que nécessaire pour atteindre les objectifs énoncés dans cette politique de confidentialité, sauf si une période de conservation plus longue est requise ou autorisée par la loi.

Changements à la politique de confidentialité : Nous nous réservons le droit de modifier cette politique de confidentialité à tout moment. Tous les changements seront effectifs dès leur publication sur notre site Web ou dans l'application. Il est de votre responsabilité de consulter régulièrement cette politique de confidentialité pour toute mise à jour.

Consentement : En utilisant notre application, vous consentez à la collecte, à l'utilisation et à la divulgation de vos informations conformément à cette politique de confidentialité.

Dernière mise à jour : 30/11/2023
'''

@app.get('/', response_model=dict)
async def start():
    """
    Point de départ de l'API.
    """
    return {'Notice': "L'API est protégée, vous ne pouvez rien faire.",
            'Un message pour vous ':"Bonjour cher développeur/utilisateur, BIENVENUE dans la politique de confidentialité de lvmh_sephora",
            'Attention':"Nous collectons certaines informations, y compris votre adresse IP et votre adresse MAC, à des fins de dépannage. Ces informations sont collectées automatiquement et anonymement et ne sont pas utilisées pour vous identifier personnellement sauf en cas de problème technique.",
            'Politique de confidentialité':Privacy_Policy}


@app.get('/api/lvmh/sephora/postgresql/getbrands/')
async def get_brands():
    """
    Obtenir la liste des marques.
    @return: Liste des marques au format JSON.
    """
    brandc = BrandsC.Brands.visualiserBrands()

    print(brandc)

    liste_brand = []

    if type(brandc) == list:
        for bc in brandc:
            brand = {
                "brand_id": bc.getBrandId(),
                "brand_name": bc.getBrandName()
            }
            liste_brand.append(brand)

        return {'response': liste_brand}

    return {'response': brandc}


@app.get('/api/lvmh/sephora/postgresql/getprodbyprice/')
async def get_prod_by_price():
    """
    Obtenir la liste des produits triés par prix.
    @return: Liste des produits triés au format JSON.
    """
    list_prods_sorted_by_price: list[ProductsM.Products] = ProductsC.Products.filtrerProdByPrice()

    liste_prods = []

    if type(list_prods_sorted_by_price) == list[ProductsM.Products]:
        for p in list_prods_sorted_by_price:
            prod = {
                "product_id": p.getProductID(),
                "product_name": p.getProductName(),
                "price": p.getPrice(),
                "stock_quantity": p.getStockQuantity()
            }
            liste_prods.append(prod)

        return {'response': liste_prods}

    else:
        return {'response': list_prods_sorted_by_price}


@app.get('/api/lvmh/sephora/postgresql/get_catalogue_prod/')
async def get_prod_catalogue():
    """
    Obtenir le catalogue complet des produits.
    @return: Catalogue des produits au format JSON.
    """
    list_prods_cat: list[dict] = ProductsC.Products.consulterCatalogueProd()

    liste_prods = []

    if type(list_prods_cat) == list[dict]:
        for cp in list_prods_cat:
            prod = {
                "product_name": cp["product_name"],
                'brand': cp["brand_name"],
                'body_part': cp["body_part"],
                'gender_name': cp["gender_name"],
                "price": cp["price"],
                "stock_quantity": cp["stock_quantity"]
            }

            liste_prods.append(prod)

        return {'response': liste_prods}

    else:
        return {"response": list_prods_cat}


@app.get('/api/lvmh/sephora/postgresql/depenses_moyenne/{idCustomer}')
async def depenses_moyennes(idCustomer: int):
    """
    Obtenir les dépenses moyennes d'un client.
    @param idCustomer: Identifiant du client.
    @return: Dépenses moyennes au format JSON.
    """
    depenses_moyenne: str | float | None = InvoicesC.Invoices.consulterdepensesmoyennes(idCustomer)

    res = {
        "depenses_moyenne": depenses_moyenne
    }

    return {'response': res}


@app.get('/api/lvmh/sephora/postgresql/cmd_by_status/{idCustomer}/{status}')
async def get_cmd_status_by_customer(idCustomer: int, status: str):
    """
    Obtenir les commandes d'un client par statut.
    @param idCustomer: Identifiant du client.
    @param status: Statut des commandes à filtrer.
    @return: Liste des commandes au format JSON.
    """
    cmd_status: str | list[OrdersM.Orders] | None = OrdersC.Orders.visualiserCMDByStatus(idCustomer, status)

    if type(cmd_status) == list:
        liste_orders = []

        for cmds in cmd_status:
            order = {
                "order_id": cmds.getOrderID(),
                'order_date': cmds.getOrderDate(),
                'order_status': cmds.getStatus()
            }

            liste_orders.append(order)

        return {'response': liste_orders}

    return {'response': cmd_status}


@app.get('/api/lvmh/sephora/postgresql/searchPleinText/{keyword}')
async def searchPleinText(keyword: str):
    """
    Rechercher des produits par texte intégral.
    @param keyword: Mot-clé pour la recherche.
    @return: Liste des produits correspondants au format JSON.
    """
    resultats: str | list[ProductsM.Products] | None = ProductsC.Products.search_product_by_name(keyword)

    if type(resultats) == list:
        liste_prods = []

        for res in resultats:
            prod = {
                "product_ID": res.getProductID(),
                "product_name": res.getProductName(),
                "price": res.getPrice(),
                "stock_quantity": res.getStockQuantity()
            }

            liste_prods.append(prod)

        return {'response': liste_prods}

    return {'response': resultats}


@app.post('/api/lvmh/sephora/postgresql/commander')
async def passer_commande(data: dict):
    """
    Passer une commande.
    @return: Réponse JSON indiquant le statut de la commande.
    """
    # Extraire les données nécessaires
    idCMD = data.get('idCMD')
    customer_id = data.get('customer_id')
    order_date = data.get('order_date')
    status = data.get('status')
    order_details = data.get('order_details', [])

    res = OrdersC.Orders.passerCMD(idCMD, customer_id, order_date, status, order_details)

    return {'response': res}


@app.post('/api/lvmh/sephora/postgresql/create_user')
async def create_user(data: dict):
    """
    Créer un nouvel utilisateur.
    @return: Réponse JSON indiquant le statut de la création.
    """
    try:
        password = data.get('password')
        username = data.get('username')

        response = sysadminC.SysAdmin.creerUnUser(password, username)

        if response == "ERROR":
            return {"response": "Erreur lors de la création de l'utilisateur."}
        else:
            return {"response": response}

    except Exception as e:
        print(f"Erreur lors de la création de l'utilisateur : {e}")
        return {"response": "Erreur interne du serveur."}


@app.post('/api/lvmh/sephora/postgresql/create_role')
async def create_role(data: dict):
    """
    Créer un nouveau rôle.
    @return: Réponse JSON indiquant le statut de la création.
    """
    try:
        role = data.get('role')

        response = sysadminC.SysAdmin.creerUnRole(role)

        if response == "ERROR":
            return {"response": "Erreur lors de la création du rôle."}
        else:
            return {"response": response}

    except Exception as e:
        print(f"Erreur de creation du rôle: {e}")
        return {"response": "Erreur interne du serveur."}

@app.post('/api/lvmh/sephora/postgresql/assign_privileges')
async def assign_privileges(data: dict):
    """
    Attribuer des privilèges à un rôle.
    @param data: Réponse JSON contenant les détails des privilèges
    @return: Réponse JSON indiquant le statut de l'attribution.
    """
    try:
        privileges = data.get('privileges')
        tables = data.get('tables')
        roles = data.get('roles')

        response = sysadminC.SysAdmin.privilege_Role(privileges, tables, roles)

        if response == "ERROR":
            return {"response": "Erreur lors de l'attribution des privilèges."}
        else:
            return {"response": response}

    except Exception as e:
        print(f"Erreur lors de l'attribution des privilèges : {e}")
        return {"response": "Erreur interne du serveur."}


@app.post('/api/lvmh/sephora/postgresql/assign_role')
async def assign_role(data: dict):
    """
    Attribuer un rôle à un utilisateur.
    @param data: Réponse JSON contenant les détails de l'attribution du rôle
    @return: Réponse JSON indiquant le statut de l'attribution.
    """
    try:
        user = data.get('user')
        roles = data.get('roles')

        response = sysadminC.SysAdmin.attribution_Role(user, roles)

        if response == "ERROR":
            return {"response": "Erreur lors de l'attribution des rôles."}
        else:
            return {"response": response}

    except Exception as e:
        print(f"Erreur lors de l'attribution des rôles : {e}")
        return {"response": "Erreur interne du serveur."}


@app.delete('/api/lvmh/sephora/postgresql/cancel_order/{order_id}')
async def cancel_order(order_id: int):
    """
    Annuler une commande.
    @param order_id: Identifiant de la commande à annuler.
    @return: Réponse JSON indiquant le statut de l'annulation.
    """
    try:
        response = OrdersC.Orders.annulerCMD(order_id)

        if response == "ERROR":
            return {"response": "Erreur lors de l'annulation de la commande."}
        else:
            return {"response": response}

    except Exception as e:
        print(f"Erreur lors de l'annulation de la commande : {e}")
        return {"response": "Erreur interne du serveur."}


@app.get('/api/lvmh/sephora/postgresql/generate_invoice/{invoice_id}')
async def generate_invoice(invoice_id: int):
    """
    Générer une facture.
    @param invoice_id: Identifiant de la facture à générer.
    @return: Réponse JSON indiquant le statut de la génération.
    """
    try:
        response = InvoicesC.Invoices.genererFacture(invoice_id)

        if response == "ERROR":
            return {"response": "Erreur lors de la génération de la facture."}
        elif type(response) == InvoicesM.Invoices:
            res = {
                "Invoices_ID": response.getInvoiceID(),
                "Order_ID": response.getOrderID().getOrderID(),
                "I_date": response.getInvoiceDate(),
                "Montant": response.getTotalAmount()
            }

            return {"response": res}

        return {"response": response}

    except Exception as e:
        print(f"Erreur lors de la génération de la facture : {e}")
        return {"response": "Erreur interne du serveur."}


if __name__ == '__main__':
    # Exécutez l'application FastAPI
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5000)
