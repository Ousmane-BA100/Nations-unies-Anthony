import os
from flask import Flask, render_template, request
from flask_cors import CORS #gestion des accès au w.s.
import json
import traceback
from datetime import datetime
from functools import wraps
from controller import ___ProductsC, ___BrandsC, BodyPartsC, ___CustomersC, GendersC, InvoicesC, OrdersC, OrderDetailsC, InvoicesC, sysadminC

from model import ProductsM, BrandsM, BodyPartsM, CustomersM, GendersM, InvoicesM, OrdersM, OrderDetailsM, InvoicesM

app = Flask(__name__)


#CORS(app, resources={fr"api/lvmh/sephora/postgresql/*": {"origins": "http://localhost:63342"}})

CORS(app, resources={fr"api/lvmh/sephora/postgresql/*": {"origins": "*"}})

LOG_FILE_PATH = '/home/keke/DataspellProjects/lvmh_sephora/utils/logs.json'

def log_request_info(route_function):
    @wraps(route_function)
    def wrapper(*args, **kwargs):
        try:
            start_time = datetime.now()

            # Exécuter la fonction de route
            response = route_function(*args, **kwargs)

            end_time = datetime.now()
            execution_time = (end_time - start_time).total_seconds()

            # Récupérer les informations de la requête
            request_info = {
                'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                'route': request.path,
                'method': request.method,
                'ip_address': request.headers.get('X-Forwarded-For', request.remote_addr),
                'execution_time': execution_time,
                'response': response
            }

            # Charger les anciens logs
            try:
                with open(LOG_FILE_PATH, 'r') as log_file:
                    logs = json.load(log_file)
            except (FileNotFoundError, json.JSONDecodeError):
                logs = []

            # Ajouter les nouveaux logs
            logs.append(request_info)

            # Enregistrer les logs dans le fichier
            with open(LOG_FILE_PATH, 'w') as log_file:
                json.dump(logs, log_file, indent=2)

            return response
        except Exception as e:
            error_message = f"Erreur lors de la journalisation de la requête : {e}"
            print(error_message)

            # Inclure les informations d'erreur dans la réponse JSON
            return {'error': 'Erreur interne du serveur', 'details': str(e), 'traceback': traceback.format_exc()}

    return wrapper

Privacy_Policy='''
Confidentiality and Security: We prioritize the protection of your information and have implemented appropriate security measures to prevent unauthorized access, disclosure, or alteration. Only authorized personnel have access to this information, and they are bound by confidentiality obligations.

Access Restrictions and Exploration: Unauthorized access to our application, including attempting to explore its functioning by accessing the root of the API, is strictly prohibited. Any violation of this privacy policy or our terms of use may result in disciplinary action, including account termination and, if necessary, legal action.

Information Retention: We retain your information for as long as necessary to fulfill the purposes stated in this privacy policy, unless a longer retention period is required or permitted by law.

Changes to the Privacy Policy: We reserve the right to modify this privacy policy at any time. Any changes will be effective upon publication on our website or within the application. It is your responsibility to regularly review this privacy policy for any updates.

Consent: By using our application, you consent to the collection, use, and disclosure of your information in accordance with this privacy policy.

Last Updated: 2023/11/30
'''


@app.route('/', methods=['GET'])
@log_request_info
def start():
    return {'Notice': "The api is protected, you could not do anything.",
            'A message for you ':"Hello dear dev./user WELCOME TO the Privacy Policy lvmh_sephora",
            'Pay attention':"We collect certain information, including your IP address and MAC address, for troubleshooting purposes. This information is collected automatically and anonymously and is not used to personally identify you unless there is a technical issue.",
            'Privacy Policy':Privacy_Policy}


@app.route(f'/api/lvmh/sephora/postgresql/getbrands/',methods=['GET'])
@log_request_info
def get_brands():
    """
    Obtenir la liste des marques.
    @return: Liste des marques au format JSON.
    """

    brandc = BrandsC.Brands.visualiserBrands()

    liste_brand = []

    if type(brandc)==list:
        for bc in brandc:

            brand = {
                "brand_id" : bc.getBrandId(),
                "brand_name" : bc.getBrandName()
            }

            liste_brand.append(brand)

        return {'response':liste_brand}

    return {'response':brandc}

@app.route(f'/api/lvmh/sephora/postgresql/getprodbyprice/',methods=['GET'])
@log_request_info
def get_prod_by_price():
    """
    Obtenir la liste des produits triés par prix.
    @return: Liste des produits triés au format JSON.
    """
    list_prods_sorted_by_price : list[ProductsM.Products] = ProductsC.Products.filtrerProdByPrice()

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

        return {'response':liste_prods}

    else :
        return {'response':list_prods_sorted_by_price}


@app.route(f'/api/lvmh/sephora/postgresql/get_catalogue_prod/',methods=['GET'])
@log_request_info
def get_prod_catalogue():
    """
    Obtenir le catalogue complet des produits.
    @return: Catalogue des produits au format JSON.
    """

    list_prods_cat : list[dict] = ProductsC.Products.consulterCatalogueProd()

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

        return {'response':liste_prods}

    else:
        return {"response": list_prods_cat}

@app.route(f'/api/lvmh/sephora/postgresql/depenses_moyenne/<idCustomer>',methods=['GET'])
@log_request_info
def depenses_moyennes(idCustomer):
    """
    Obtenir les dépenses moyennes d'un client.
    @param idCustomer: Identifiant du client.
    @return: Dépenses moyennes au format JSON.
    """

    depenses_moyenne: str | float | None = InvoicesC.Invoices.consulterdepensesmoyennes(idCustomer)

    res = {
        "depenses_moyenne" : depenses_moyenne
    }

    return {'response':res}

@app.route(f'/api/lvmh/sephora/postgresql/cmd_by_status/<idCustomer>/<status>',methods=['GET'])
@log_request_info
def get_cmd_status_by_customer(idCustomer, status):
    """
    Obtenir les commandes d'un client par statut.
    @param idCustomer: Identifiant du client.
    @param status: Statut des commandes à filtrer.
    @return: Liste des commandes au format JSON.
    """

    cmd_status: str | list[OrdersM.Orders] | None = OrdersC.Orders.visualiserCMDByStatus(int(idCustomer), status)

    if type(cmd_status)==list:

        liste_orders = []

        for cmds in cmd_status:
            order = {
                "order_id": cmds.getOrderID(),
                'order_date': cmds.getOrderDate(),
                'order_status': cmds.getStatus()
            }

            liste_orders.append(order)

        return {'response':liste_orders}

    return {'response':cmd_status}

@app.route(f'/api/lvmh/sephora/postgresql/searchPleinText/<keyword>',methods=['GET'])
@log_request_info
def searchPleinText(keyword):
    """
    Rechercher des produits par texte intégral.
    @param keyword: Mot-clé pour la recherche.
    @return: Liste des produits correspondants au format JSON.
    """
    resultats: str | list[ProductsM.Products] | None = ProductsC.Products.search_product_by_name(keyword)

    if type(resultats)==list:

        liste_prods = []

        for res in resultats:
            prod = {
                "product_ID": res.getProductID(),
                "product_name": res.getProductName(),
                "price": res.getPrice(),
                "stock_quantity":  res.getStockQuantity()
            }

            liste_prods.append(prod)

        return {'response':liste_prods}


    return {'response':resultats}

@app.route(f'/api/lvmh/sephora/postgresql/commander', methods=['POST'])
@log_request_info
def passer_commande():
    """
    Passer une commande.
    @return: Réponse JSON indiquant le statut de la commande.
    """
    data = request.json  # Récupère les données JSON du corps de la requête

    # Extraire les données nécessaires
    idCMD = data.get('idCMD')
    customer_id = data.get('customer_id')
    order_date = data.get('order_date')
    status = data.get('status')
    #invoices_id = data.get('invoices_id')
    order_details = data.get('order_details', [])

    res = OrdersC.Orders.passerCMD(idCMD, customer_id, order_date,
                                   status, order_details)

    return {'response': res}

# Route pour créer un utilisateur
@app.route('/api/lvmh/sephora/postgresql/create_user', methods=['POST'])
@log_request_info
def create_user():
    """
    Créer un nouvel utilisateur.
    @return: Réponse JSON indiquant le statut de la création.
    """
    try:
        password = request.json.get('password')
        username = request.json.get('username')

        response = sysadminC.SysAdmin.creerUnUser(password, username)

        if response == "ERROR":
            return {"response": "Erreur lors de la création de l'utilisateur."}
        else:
            return {"response": response}

    except Exception as e:
        print(f"Erreur lors de la création de l'utilisateur : {e}")
        return {"response": "Erreur interne du serveur."}

# Route pour créer un rôle
@app.route('/api/lvmh/sephora/postgresql/create_role', methods=['POST'])
@log_request_info
def create_role():
    """
    Créer un nouveau rôle.
    @return: Réponse JSON indiquant le statut de la création.
    """
    try:
        role = request.json.get('role')

        response = sysadminC.SysAdmin.creerUnRole(role)

        if response == "ERROR":
            return {"response": "Erreur lors de la création du rôle."}
        else:
            return {"response": response}

    except Exception as e:
        print(f"Erreur lors de la création du rôle : {e}")
        return {"response": "Erreur interne du serveur."}

@app.route('/api/lvmh/sephora/postgresql/assign_privileges', methods=['POST'])
@log_request_info
def assign_privileges():
    """
    Attribuer des privilèges à un rôle.
    @return: Réponse JSON indiquant le statut de l'attribution.
    """
    try:
        privileges = request.json.get('privileges')
        tables = request.json.get('tables')
        roles = request.json.get('roles')

        response = sysadminC.SysAdmin.privilege_Role(privileges, tables, roles)

        if response == "ERROR":
            return {"response": "Erreur lors de l'attribution des privilèges."}
        else:
            return {"response": response}

    except Exception as e:
        print(f"Erreur lors de l'attribution des privilèges : {e}")
        return {"response": "Erreur interne du serveur."}

# Route pour attribuer un rôle à un utilisateur
@app.route('/api/lvmh/sephora/postgresql/assign_role', methods=['POST'])
@log_request_info
def assign_role():
    """
    Attribuer un rôle à un utilisateur.
    @return: Réponse JSON indiquant le statut de l'attribution.
    """
    try:
        user = request.json.get('user')
        roles = request.json.get('roles')

        response = sysadminC.SysAdmin.attribution_Role(user, roles)

        if response == "ERROR":
            return {"response": "Erreur lors de l'attribution des rôles."}
        else:
            return {"response": response}

    except Exception as e:
        print(f"Erreur lors de l'attribution des rôles : {e}")
        return {"response": "Erreur interne du serveur."}

# Route pour annuler une commande
@app.route('/api/lvmh/sephora/postgresql/cancel_order/<order_id>', methods=['DELETE'])
@log_request_info
def cancel_order(order_id):
    """
    Annuler une commande.
    @param order_id: Identifiant de la commande à annuler.
    @return: Réponse JSON indiquant le statut de l'annulation.
    """
    try:
        response = OrdersC.Orders.annulerCMD(int(order_id))

        if response == "ERROR":
            return {"response": "Erreur lors de l'annulation de la commande."}
        else:
            return {"response": response}

    except Exception as e:
        print(f"Erreur lors de l'annulation de la commande : {e}")
        return {"response": "Erreur interne du serveur."}

# Route pour générer une facture
@app.route('/api/lvmh/sephora/postgresql/generate_invoice/<invoice_id>', methods=['GET'])
@log_request_info
def generate_invoice(invoice_id):
    """
    Générer une facture.
    @param invoice_id: Identifiant de la facture à générer.
    @return: Réponse JSON indiquant le statut de la génération.
    """
    try:
        response = InvoicesC.Invoices.genererFacture(int(invoice_id))

        if response == "ERROR":
            return {"response": "Erreur lors de la génération de la facture."}
        elif type(response)==InvoicesM.Invoices:
            res = {
                "Invoices_ID":response.getInvoiceID(),
                "Order_ID":response.getOrderID().getOrderID(),
                "I_date":response.getInvoiceDate(),
                "Montant":response.getTotalAmount()
            }

            return {"response": res}

        return {"response": response}

    except Exception as e:
        print(f"Erreur lors de la génération de la facture : {e}")
        return {"response": "Erreur interne du serveur."}

if __name__=='__main__':

    # Run flask with the following defaults
    app.run(debug=True, port=5000, host='0.0.0.0', )