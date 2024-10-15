from flask import Blueprint
from flask import jsonify, make_response, request

from app.models import Producto
from app.services import CatalogoService

catalogo = Blueprint('catalogo', __name__)

catalogo_service = CatalogoService()

@catalogo.route('/get_all', methods=['GET'])
def get_all():
    productos = catalogo_service.get_all()
    return productos


@catalogo.route('/get_by_id/<int:id>', methods=['GET'])
def get_by_id(id: int):
    print("SOY CATALOGO :)")
    producto = catalogo_service.get_by_id(id)
    print(producto)
    if producto:
        resp = jsonify({
            'id': producto.id,
            'nombre': producto.nombre,
            'precio': producto.precio,
            'activado': producto.activado
        })
        return make_response(resp)
    else:
        return make_response(jsonify(f'El producto id={id} no existe.')), 200
    
@catalogo.route('/add', methods=['POST'])
def add():
    datos_producto = request.get_json()

    producto = Producto(**datos_producto)
    catalogo_service.add(producto)
    return jsonify('Producto insertado en la BD')

    

