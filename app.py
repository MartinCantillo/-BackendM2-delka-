from flask import Flask
from flask_cors import CORS
from config.bd import app

from api.UsuarioApi import ruta_usuario
from api.CategoriaApi import ruta_categoria
from api.ProductoApi import ruta_producto

from api.CarroCompraApi import ruta_carroCompra
from api.ProductoCarroCApi import ruta_ProductocarroCompra

app.register_blueprint(ruta_usuario, url_prefix="/api")
app.register_blueprint(ruta_categoria, url_prefix="/api")
app.register_blueprint(ruta_producto, url_prefix="/api")
app.register_blueprint(ruta_carroCompra, url_prefix="/api")
app.register_blueprint(ruta_ProductocarroCompra, url_prefix="/api")

@app.route("/")
def index():
    return "Hola world"

CORS(app)

#if __name__ == "__main__":
 #   app.run(debug=True, port=5000, host="0.0.0.0")