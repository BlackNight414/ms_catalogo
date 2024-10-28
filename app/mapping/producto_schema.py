from marshmallow import Schema, fields, post_load
from app.models import Producto

class ProductoSchema(Schema):
    id: int = fields.Integer(dump_only=True)
    nombre: str = fields.String(required=True)
    precio: float = fields.Float(required=True)
    activado: bool = fields.Boolean(load_default=True)

    @post_load
    def deserializar_producto(self, data, **kwargs):
        return Producto(**data)
