from flask import Flask, Blueprint, request, jsonify
from config.Token import generate_token
from config.bd import app, bd, ma
from models.ProductoCarroc import ProductoCarroC, ProductoCarroCSchema
from config.routeProtection import token_required

ruta_ProductocarroCompra = Blueprint("ruta_ProductocarroCompra", __name__)

productoCarroC_schema = ProductoCarroCSchema()
productoCarroCs_schema = ProductoCarroCSchema(many=True)


@ruta_ProductocarroCompra.route('/agregar', methods=['POST'])
@token_required
def agregar_producto_carro_compra(current_user):
    IdProducto = request.json["IdProducto"]
    IdCarroCompra = request.json["IdCarroCompra"]

    nuevo_producto_carro = ProductoCarroC(IdProducto=IdProducto, IdCarroCompra=IdCarroCompra)
    bd.session.add(nuevo_producto_carro)
    bd.session.commit()

    return productoCarroC_schema.jsonify(nuevo_producto_carro)


@ruta_ProductocarroCompra.route('/eliminarproductocaro', methods=['POST'])
@token_required
def eliminar_producto_carro_compra():
    id = request.json['id']
    producto_carro_eliminar = ProductoCarroC.query.get(id)
    if not producto_carro_eliminar:
        return jsonify({"message": "Producto en carro de compra no encontrado"}), 404

    bd.session.delete(producto_carro_eliminar)
    bd.session.commit()

    return productoCarroC_schema.jsonify(producto_carro_eliminar)

@ruta_ProductocarroCompra.route('/obtenerIdcarroCompra', methods=['POST'])
@token_required
def obtener_productos_carro_compra():
    id_carro_compra = request.json['id_carro_compra']
    productos_carro_compra = ProductoCarroC.query.filter_by(IdCarroCompra=id_carro_compra).all()

    return productoCarroCs_schema.jsonify.dump(productos_carro_compra)