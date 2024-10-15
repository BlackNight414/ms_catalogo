from app import db 

class Producto(db.Model):

    __tablename__ = 'productos'

    id: int = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    nombre: str = db.Column('nombre', db.String(120), nullable=False)
    precio: float = db.Column('precio', db.Float, nullable=False)
    activado: bool = db.Column('activado', db.Boolean, nullable=False)