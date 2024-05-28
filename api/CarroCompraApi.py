from flask import Flask, Blueprint, request, jsonify
from config.Token import generate_token
from config.bd import app, bd, ma
from models.CarroCompra import CarroCompra, CarroCompraSchema
from config.routeProtection import token_required


ruta_carroCompra = Blueprint("ruta_carroCompra", __name__)


carroCompra_schema = CarroCompraSchema()
carroCompras_schema = CarroCompraSchema(many=True)

@ruta_carroCompra.route("/carroCompra", methods=["POST"])
@token_required
def add_carro_compra():
    nombre = request.json['nombre']
    cantidad =request.json['cantidad']
    IdProducto = request.json['IdProducto']
    IdUsuario = request.json['IdUsuario']
    total = request.json['total']

    if not nombre or not cantidad or not IdProducto or not IdUsuario or not total:
        return jsonify({"message": "All fields are required"}), 400

    nuevo_carro_compra = CarroCompra(nombre, cantidad, IdProducto, total)
    nuevo_carro_compra.IdUsuario = IdUsuario
    bd.session.add(nuevo_carro_compra)
    bd.session.commit()

    return carroCompra_schema.jsonify(nuevo_carro_compra), 201


@ruta_carroCompra.route("/carroCompraByUsuario", methods=["GET"])
@token_required
def get_carro_compra_by_usuario():
    IdUsuario = request.json['IdUsuario']
    if not IdUsuario:
        return jsonify({"message": "IdUsuario is required"}), 400

    try:
        IdUsuario = int(IdUsuario)
    except ValueError:
        return jsonify({"message": "Invalid IdUsuario format"}), 400

    carro_compras = CarroCompra.query.filter_by(IdUsuario=IdUsuario).all()
    if carro_compras:
        return carroCompras_schema.jsonify.dump(carro_compras)
    else:
        return jsonify({"message": "No purchases found for this user"}), 404

@ruta_carroCompra.route("/carroCompras", methods=["GET"])
@token_required
def get_all_carro_compras():
    carro_compras = CarroCompra.query.all()
    result = carroCompras_schema.dump(carro_compras)
    return jsonify(result)