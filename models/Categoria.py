from config.bd import bd, app, ma

class Categoria(bd.Model):
    __tablename__ = 'tblCategoria'
    id = bd.Column(bd.Integer, primary_key=True)
    nombre = bd.Column(bd.String(50))
    descripcion = bd.Column(bd.String(50))
    recomendacion=bd.Column(bd.String(50))
    
    def __init__(self, nombre, descripcion):
        self.nombre = nombre
        self.descripcion = descripcion

with app.app_context():
    bd.create_all()

class CategoriaSchema(ma.Schema):
    class Meta:
        
        fields = ("idCategoria", "nombre", "descripcion") 
