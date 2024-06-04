from flask import Flask, Blueprint, request, jsonify
from config.Token import generate_token
from config.bd import app, bd, ma
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
    idCategoria = request.json['idCategoria']
    adquirido = request.json['adquirido']
    idUsuario = request.json['idUsuario']

    nuevo_producto = Producto(nombre, prioridad, nota, precio,idCategoria,adquirido,idUsuario)
    bd.session.add(nuevo_producto)
    bd.session.commit()

    return producto_schema.jsonify(nuevo_producto)

@ruta_producto.route('/eliminarProducto', methods=['DELETE'])
@token_required
def delete_producto():
    id = request.json['id']
    producto = Producto.query.get(id)
    if producto is None:
        return jsonify({"message": "Producto no encontrado"}), 404

    bd.session.delete(producto)
    bd.session.commit()

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
    bd.session.commit()
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
    bd.session.commit()
    return producto_schema.jsonify(producto)


@ruta_producto.route('/editarAdquirido', methods=['POST'])
@token_required
def editar_adquirido():
    adquirido = request.json['adquirido']
    id = request.json['id']
    producto = Producto.query.get(id)
    if producto is None:
        return jsonify({"message": "Producto no encontrado"}), 404

    producto.adquirido = adquirido
    bd.session.commit()
    return producto_schema.jsonify(producto)



@ruta_producto.route('/getProductosPorCategoria', methods=['POST'])
@token_required
def get_productos_por_categoria():
    idCategoria = request.json['idCategoria']
    idUsuario = request.json['idUsuario']
    productos = Producto.query.filter_by(idCategoria=idCategoria,idUsuario=idUsuario).all()
    result = productos_schema.dump(productos)
    return jsonify(result)