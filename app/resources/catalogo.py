from flask import Blueprint
from flask import jsonify, make_response, request

from app.models import Producto
from app.services import CatalogoService
from app.mapping import ProductoSchema

catalogo = Blueprint('catalogo', __name__)

catalogo_service = CatalogoService()
producto_schema = ProductoSchema()

@catalogo.route('/get_all', methods=['GET'])
def get_all():
    productos = catalogo_service.get_all()
    return producto_schema.dump(productos, many=True), 200
    
@catalogo.route('/get_by_id/<int:id>', methods=['GET'])
def get_by_id(id: int):

    producto = catalogo_service.get_by_id(id)

    if producto:
        return producto_schema.dump(producto), 200
    else:
        return make_response(jsonify({'msg': 'NOT FOUND'})), 200
    
@catalogo.route('/registrar_producto', methods=['POST'])
def registrar_producto():
    datos_producto = request.get_json()

    try:
        producto = catalogo_service.registrar_producto(producto_schema.load(datos_producto))
        return producto_schema.dump(producto), 200
    except Exception as e:
        print(e)
        return jsonify('No se pudo insertar el producto'), 500

    

