from app.repositories import CatalogoRepository
from app.models import Producto

class CatalogoService:

    def __init__(self):
        self.catalogo_repository = CatalogoRepository()

    def add(self, producto: Producto):
        return self.catalogo_repository.add(producto)

    def get_all(self):
        return self.catalogo_repository.get_all()

    def get_by_id(self, id: int):
        return self.catalogo_repository.get_by_id(id)