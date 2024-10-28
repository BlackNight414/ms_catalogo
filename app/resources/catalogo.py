from flask import Blueprint
from flask import jsonify, make_response, request

from app.models import Producto
from app.services import CatalogoService
from app import cache
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

    # Duda: ¿Cache idealmente va en las rutas o en los métodos de services?
    producto = cache.get(f'producto_id_{id}')
    if producto is None:
        producto = catalogo_service.get_by_id(id)
        cache.set(f'producto_id_{producto.id}', producto, timeout=60)

    if producto:
        return producto_schema.dump(producto), 200
    else:
        return make_response(jsonify({'msg': 'NOT FOUND'})), 200
    
@catalogo.route('/registrar_producto', methods=['POST'])
def registrar_producto():
    datos_producto = request.get_json()

    try:
        producto = catalogo_service.registrar_producto(producto_schema.load(datos_producto))
        return producto_schema.dump(), 200
    except:
        return jsonify('No se pudo insertar el producto'), 500

    

