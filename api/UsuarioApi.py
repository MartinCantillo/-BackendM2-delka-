from flask import Flask, Blueprint, request, jsonify
from config.Token import generate_token
from config.bd import app, bd, ma
from models.Usuario import Usuario, UserSchema
from config.routeProtection import token_required

ruta_usuario = Blueprint("ruta_usuario", __name__)

usuario_schema = UserSchema()
usuarios_schema = UserSchema(many=True)

@ruta_usuario.route("/saveUser", methods=['POST'])
def saveUser():
    username = request.json['username']
    password = request.json['password']

    if not username or not password:
        return jsonify({'message': 'Missing username or password'}), 400

    new_user = Usuario(username=username, password=password)
    bd.session.add(new_user)
    bd.session.commit()

    user_id = new_user.id

    return jsonify({'message': 'User saved', 'user_id': user_id}), 200


@ruta_usuario.route("/login", methods=['POST'])
def login():
    username = request.json['username']
    password = request.json['password']

    if not username or not password:
        return jsonify({"message": "Username and password are required"}), 400

    user = Usuario.query.filter_by(username=username).first()

    if not user:
        return jsonify({"message": "Invalid username or password"}), 401


    if user.password != password:
        return jsonify({"message": "Invalid username or password"}), 401

    # Generar token JWT
    token = generate_token(user.id, user.username)


    return jsonify({"user_id": user.id,"token": token["token"]}), 200