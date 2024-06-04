from config.bd import bd, app, ma

class Producto(bd.Model):
    __tablename__ = 'tblProducto'
    id = bd.Column(bd.Integer, primary_key=True)
    nombre = bd.Column(bd.String(50))
    prioridad = bd.Column(bd.String(50))
    nota = bd.Column(bd.String(50))
    precio = bd.Column(bd.Float)
    adquirido =bd.Column(bd.String(50))
    idCategoria = bd.Column(bd.Integer, bd.ForeignKey("tblCategoria.id"))
    idUsuario= bd.Column(bd.Integer, bd.ForeignKey("tblUsuario.id"))
    def __init__(self, nombre, prioridad, nota, precio,idCategoria,adquirido,idUsuario):
        self.nombre = nombre
        self.prioridad = prioridad
        self.nota = nota
        self.precio = precio
        self.idCategoria=idCategoria
        self.adquirido=adquirido
        self.idUsuario=idUsuario

with app.app_context():
    bd.create_all()

class ProductoSchema(ma.Schema):
    class Meta:
        fields = ("id", "nombre", "prioridad", "nota", "precio","adquirido","idCategoria","idUsuario")
