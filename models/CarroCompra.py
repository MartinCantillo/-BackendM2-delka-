from config.bd import bd, app, ma

class CarroCompra(bd.Model):
    __tablename__ = 'tblCarroCompra'

    id = bd.Column(bd.Integer, primary_key=True)
    nombre = bd.Column(bd.String(50))
    cantidad = bd.Column(bd.Integer)
    #IdProductoCarroC = bd.Column(bd.Integer, bd.ForeignKey("tblProductoCarroC.id"))
    IdUsuario = bd.Column(bd.Integer, bd.ForeignKey("tblUsuario.id"))
    total = bd.Column(bd.Float)

    def __init__(self, nombre, cantidad , total):
        self.nombre = nombre
        self.cantidad = cantidad
        self.total = total

with app.app_context():
    bd.create_all()

class CarroCompraSchema(ma.Schema):
    class Meta:
    
        fields = ("id", "nombre", "cantidad", "total")  
