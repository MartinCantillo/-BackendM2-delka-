from config.bd import bd, app, ma

class Producto(bd.Model):
    __tablename__ = 'tblProducto'
    id = bd.Column(bd.Integer, primary_key=True)
    nombre = bd.Column(bd.String(50))
    prioridad = bd.Column(bd.String(50))
    nota = bd.Column(bd.String(50))
    precio = bd.Column(bd.Float)  
    IdCategoria = bd.Column(bd.Integer, bd.ForeignKey("tblCategoria.id"))
    def __init__(self, nombre, prioridad, nota, precio,IdCategoria):
        self.nombre = nombre
        self.prioridad = prioridad
        self.nota = nota
        self.precio = precio
        self.IdCategoria=IdCategoria

with app.app_context():
    bd.create_all()

class ProductoSchema(ma.Schema):
    class Meta:
        fields = ("id", "nombre", "prioridad", "nota", "precio","IdCategoria") 
