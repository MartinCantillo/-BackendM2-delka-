from flask import Flask, Blueprint, request, jsonify
from Config.Token import generate_token
from Config.bd import app, bd, ma
from Models.Producto import Producto, ProductoSchema
from Config.routeProtection import token_required

ruta_producto = Blueprint("ruta_producto", __name__)

producto_schema = ProductoSchema()
productos_schema = ProductoSchema(many=True)


@ruta_producto.route('/getProductos', methods=['GET'])
@token_required
def get_productos():
    productos = Producto.query.all()
    result = productos_schema.dump(productos)
    return jsonify(result)


@ruta_producto.route('/addProducto', methods=['POST'])
@token_required
def add_producto():
    nombre = request.json['nombre']
    prioridad =request.json['prioridad']
    nota = request.json['nota']
    precio = request.json['precio']
    IdCategoria = request.json['IdCategoria']

    nuevo_producto = Producto(nombre, prioridad, nota, precio, IdCategoria)
    bd.session.add(nuevo_producto)
    bd.session.commit()

    return producto_schema.jsonify(nuevo_producto)


@ruta_producto.route('/eliminarProducto', methods=['DELETE'])
@token_required
def delete_producto(id):

    id = request.json['id']
    producto = Producto.query.get(id)
    if producto is None:
        return jsonify({"message": "Producto no encontrado"}), 404

    bd.session.delete(producto)
    bd.session.commit()

    return jsonify({"message": "Producto eliminado"}), 200



