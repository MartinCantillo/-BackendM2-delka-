from flask import Flask, Blueprint, request, jsonify
from config.Token import generate_token
from config.bd import app, db, ma
from models.Producto import Producto, ProductoSchema
from config.routeProtection import token_required

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
    prioridad = request.json['prioridad']
    nota = request.json['nota']
    precio = request.json['precio']
    IdCategoria = request.json['IdCategoria']

    nuevo_producto = Producto(nombre, prioridad, nota, precio, IdCategoria, False)
    db.session.add(nuevo_producto)
    db.session.commit()

    return producto_schema.jsonify(nuevo_producto)

@ruta_producto.route('/eliminarProducto', methods=['DELETE'])
@token_required
def delete_producto():
    id = request.json['id']
    producto = Producto.query.get(id)
    if producto is None:
        return jsonify({"message": "Producto no encontrado"}), 404

    db.session.delete(producto)
    db.session.commit()

    return jsonify({"message": "Producto eliminado"}), 200

@ruta_producto.route('/editarPrioridad', methods=['POST'])
@token_required
def editar_prioridad():
    nueva_prioridad = request.json['prioridad']
    id = request.json['id']
    producto = Producto.query.get(id)
    if producto is None:
        return jsonify({"message": "Producto no encontrado"}), 404

    producto.prioridad = nueva_prioridad
    db.session.commit()
    return producto_schema.jsonify(producto)

@ruta_producto.route('/editarNota', methods=['POST'])
@token_required
def editar_nota(id):
    nueva_nota = request.json['nota']
    id = request.json['id']
    producto = Producto.query.get(id)
    if producto is None:
        return jsonify({"message": "Producto no encontrado"}), 404

    producto.nota = nueva_nota
    db.session.commit()
    return producto_schema.jsonify(producto)


@ruta_producto.route('/editarAdquirido', methods=['POST'])
@token_required
def editar_adquirido(id):
    adquirido = request.json['adquirido']
    id = request.json['id']
    producto = Producto.query.get(id)
    if producto is None:
        return jsonify({"message": "Producto no encontrado"}), 404

    producto.adquirido = adquirido
    db.session.commit()
    return producto_schema.jsonify(producto)