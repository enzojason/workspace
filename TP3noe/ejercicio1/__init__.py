from flask import Flask, request
from config import Config
from .database import DatabaseConnection
def init_app():
    """Crea y configura la aplicacion Flask"""
    app = Flask(__name__, static_folder = Config.STATIC_FOLDER, template_folder = Config.TEMPLATE_FOLDER)
    app.config.from_object(Config)
    #Ejercio 1.1: Obtener un cliente.
    @app.route('/customers/<int:customer_id>', methods = ['GET'])
    def customer(customer_id):
        query = "SELECT customer_id, first_name, last_name, phone, email, city, street, state, zip_code FROM sales.customers WHERE customers_id = %s; "
        params = customer_id
        result = DatabaseConnection.fetch_one(query, params)
        if result is not None:
            return {
                "id": result[0],
                "nombre": result[1],
                "apellido": result[2],
                
            }, 200        
        return {'msg':"No se encontró el cliente"}, 404
    #Ejercio 1.2: Obtener el listado de clientes.
    @app.route('/customers', methods = ['GET'])
    def listado_clientes():
        query = "SELECT customer_id, total FROM "
        return""
    #Ejercicio 1.3: Registrar un cliente.
    @app.route('/customers', methods = ['POST'])
    def get_customer():
        return""
    #Ejercicio 1.4: Modificar un clieinte.
    @app.route('/customers/<int:customer_id>', methods = ["PUT"])
    def put_customer():
        return""
    #Ejercicio 1.5: Eliminar un cliente.
    @app.route('/customers/<int:customer_id>', methods = ["DELETE"])
    def delete_customer():
        return""
    
    return app