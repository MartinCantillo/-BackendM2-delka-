from flask import Flask, Blueprint, request, jsonify
from config.Token import generate_token
from config.bd import app, bd, ma
from models.Categoria import Categoria, CategoriaSchema
from config.routeProtection import token_required


ruta_categoria = Blueprint("ruta_categoria", __name__)


categoria_schema = CategoriaSchema()
categorias_schema = CategoriaSchema(many=True)


@ruta_categoria.route('/obtenercategorias', methods=['GET'])
@token_required
def get_categorias():
    categorias = Categoria.query.all()
    result = categorias_schema.dump(categorias)
    return jsonify.dump(result)


@ruta_categoria.route('/agregarcategoria', methods=['POST'])
@token_required
def add_categoria():
    nombre = request.json['nombre']
    descripcion = request.json['descripcion']

    nueva_categoria = Categoria(nombre, descripcion)
    bd.session.add(nueva_categoria)
    bd.session.commit()

    return categoria_schema.jsonify(nueva_categoria)


@ruta_categoria.route('/eliminarcategoria', methods=['DELETE'])
@token_required
def delete_categoria(id):
    id = request.json['id']
    categoria = Categoria.query.get(id)
    if categoria is None:
        return jsonify({"message": "Categoría no encontrada"}), 404

    bd.session.delete(categoria)
    bd.session.commit()

    return jsonify({"message": "Categoría eliminada"}), 200