from flask import Blueprint
from flask import jsonify, make_response, request

from app.models import Producto
from app.services import CatalogoService
from app import cache

catalogo = Blueprint('catalogo', __name__)

catalogo_service = CatalogoService()

@catalogo.route('/get_all', methods=['GET'])
def get_all():
    productos = catalogo_service.get_all()
    return productos


@catalogo.route('/get_by_id/<int:id>', methods=['GET'])
def get_by_id(id: int):

    # Duda: ¿Cache idealmente va en las rutas o en los métodos de services?
    producto = cache.get(f'producto_id_{id}')
    if producto is None:
        producto = catalogo_service.get_by_id(id)
        cache.set(f'producto_id_{producto.id}', producto, timeout=60)

    if producto:
        resp = jsonify({
            'id': producto.id,
            'nombre': producto.nombre,
            'precio': producto.precio,
            'activado': producto.activado
        })
        return make_response(resp), 200
    else:
        return make_response(jsonify({'msg': 'NOT FOUND'})), 200
    
@catalogo.route('/add', methods=['POST'])
def add():
    datos_producto = request.get_json()

    producto = Producto(**datos_producto)
    catalogo_service.add(producto)
    return jsonify('Producto insertado en la BD')

    

