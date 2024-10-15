from app import db
from app.models import Producto

class CatalogoRepository:

    def add(self, producto: Producto):
        """ Agrega un producto """
        db.session.add(producto)
        db.session.commit()
        return producto

    def get_all(self):
        return db.session.query(Producto).all()

    def get_by_id(self, id: int):
        """ Obtiene un producto por su id """
        return db.session.query(Producto).filter(Producto.id==id).first()
    
    

