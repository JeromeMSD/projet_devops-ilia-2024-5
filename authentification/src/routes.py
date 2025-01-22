from flask import request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from config import app, db
from models.example_model import User


@jwt_required()
def refresh_token_if_needed():
    current_user = get_jwt_identity()
    new_token = create_access_token(identity=current_user)
    return jsonify({"new_token": new_token}), 200


# Endpoint pour l'incription
@app.route("/auth/sign_in", methods=["POST"])
def sign_in():
    data = request.get_json()
    if not data:
        return jsonify({"message": "Données manquantes"}), 400

    nom = data.get("nom")
    prenom = data.get("prenom")
    email = data.get("email")
    password = data.get("password")
    username = data.get("username")
    pseudo = data.get("pseudo")

    if not all([nom, prenom, email, password, username, pseudo]):
        return jsonify({"message": "Tous les champs sont obligatoires"}), 400

    if User.query.filter_by(username=username).first() or User.query.filter_by(email=email).first():
        return jsonify({"message": "Nom d'utilisateur ou email déjà utilisé"}), 409

    new_user = User(nom=nom, prenom=prenom, email=email, password=password, username=username, pseudo=pseudo)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "Utilisateur créé avec succès"}), 200


# Endpoint pour la connexion
@app.route("/auth/login", methods=["POST"])
def login():
    data = request.get_json()
    username_or_email = data.get("username_or_email")
    password = data.get("password")

    if not username_or_email or not password:
        return jsonify({"message": "Nom d'utilisateur ou mot de passe requis"}), 400

    user = User.query.filter((User.username == username_or_email) | (User.email == username_or_email)).first()
    if user and user.password == password:
        access_token = create_access_token(identity=user.username)
        return jsonify({"token": access_token}), 200

    return jsonify({"message": "Nom d'utilisateur ou mot de passe incorrect"}), 401


# Endpoint pour récupérer les informations d'un utilisateur
@app.route("/users/<username>", methods=["GET"])
@jwt_required()
def get_user(username):
    user = User.query.filter_by(username=username).first()
    if not user:
        return jsonify({"message": "Utilisateur non trouvé"}), 404

    return jsonify(user.basic_info()), 200


# Endpoint pour supprimer un utilisateur
@app.route("/users/<username>", methods=["DELETE"])
@jwt_required()
def delete_user(username):
    try:
        current_user = get_jwt_identity()
        if current_user != username:
            return jsonify({"message": "Accès non autorisé"}), 403

        user = User.query.filter_by(username=username).first()
        if not user:
            return jsonify({"message": "Utilisateur non trouvé"}), 404

        db.session.delete(user)
        db.session.commit()
        return jsonify({"message": "Utilisateur supprimé"}), 200
    except Exception as e:
        return jsonify({"message": "Erreur interne du serveur", "error": str(e)}), 500


# Endpoint pour mettre à jour les informations de l'utilisateur
@app.route("/users/<username>", methods=["PUT"])
@jwt_required()
def update_user(username):
    try:
        current_user = get_jwt_identity()
        if current_user != username:
            return jsonify({"message": "Accès non autorisé"}), 403

        data = request.get_json()

        user = User.query.filter_by(username=username).first()
        if not user:
            return jsonify({"message": "Utilisateur non trouvé"}), 404

        # Mise à jour des informations de l'utilisateur
        user.nom = data.get("nom", user.nom)
        user.prenom = data.get("prenom", user.prenom)
        user.email = data.get("email", user.email)
        user.password = data.get("password", user.password)
        user.pseudo = data.get("pseudo", user.pseudo)

        db.session.commit()
        return jsonify(user.to_dict()), 200

    except Exception as e:
        return jsonify({"message": "Erreur interne du serveur", "error": str(e)}), 500
