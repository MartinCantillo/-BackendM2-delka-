from config.bd import bd, app, ma

class ProductoCarroC(bd.Model):
    __tablename__ = 'tblProductoCarroC'
    id = bd.Column(bd.Integer, primary_key=True)
    IdProducto = bd.Column(bd.Integer, bd.ForeignKey("tblProducto.id"))
    IdCarroCompra = bd.Column(bd.Integer, bd.ForeignKey("tblCarroCompra.id"))
    def __init__(self, IdProducto, IdCarroCompra):
        self.IdProducto = IdProducto
        self.IdCarroCompra = IdCarroCompra
      

with app.app_context():
    bd.create_all()

class ProductoCarroCSchema(ma.Schema):
    class Meta:
        fields = ("id", "IdCarroCompra", "IdProducto") 
