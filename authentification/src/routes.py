from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from config import db, app
from models.user import User

route = Blueprint('routes', __name__, static_folder='static', template_folder='templates')

@jwt_required()
def refresh_token_if_needed():
    current_user = get_jwt_identity()
    new_token = create_access_token(identity=current_user)
    return jsonify({"new_token": new_token}), 200


# Endpoint pour l'incription
@route.route("/auth/sign_in", methods=["POST"])
def sign_in():
    data = request.get_json()
    if not data:
        return jsonify({"message": "Données manquantes"}), 400

    nom = data.get("lastName")
    prenom = data.get("firstName")
    email = data.get("email")
    password = data.get("password")
    username = data.get("username")
    pseudo = data.get("pseudo")

    if not all([nom, prenom, email, password, username, pseudo]):
        return jsonify({"message": "Tous les champs sont obligatoires"}), 400

    if User.query.filter_by(username=username).first():
        return jsonify({"message": "Nom d'utilisateur déjà utilisé"}), 409
    elif  User.query.filter_by(email=email).first():
        return jsonify({"message": "Email déjà utilisé"}), 409

    new_user = User(last_name=nom, first_name=prenom, email=email, username=username, pseudo=pseudo)
    new_user.set_password(password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "Utilisateur créé avec succès"}), 200


# Endpoint pour la connexion
@route.route("/auth/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data.get("username")
    email = data.get("email")
    id = ""
    if not username and email:
        id = email
    elif not email and username:
        id = username
    else:
         return jsonify({"message": "Nom d'utilisateur (ou l'email) requis"}), 400

    password = data.get("password")

    if not password:
        return jsonify({"message": "Nom d'utilisateur ou mot de passe requis"}), 400

    user = User.query.filter((User.username == id) | (User.email == id)).first()
    if user and user.check_password(password):
        access_token = create_access_token(identity=user.username)
        return jsonify({"token": access_token}), 200

    return jsonify({"message": "Nom d'utilisateur ou mot de passe incorrect"}), 401


# Endpoint pour récupérer les informations d'un utilisateur
@route.route("/users/<username>", methods=["GET"])
@jwt_required(optional=True)
def get_user(username):
    user = User.query.filter_by(username=username).first()
    if not user:
        return jsonify({"message": "Utilisateur non trouvé"}), 404

    current_identity = get_jwt_identity()
    if current_identity:
        if current_identity != username:
            return jsonify({"message": "Accès non autorisé"}), 403
        return jsonify(user.to_dict()), 200
    else:
        return jsonify(user.to_dict_min()), 200

# Endpoint pour supprimer un utilisateur
@route.route("/users/<username>", methods=["DELETE"])
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
@route.route("/users/<username>", methods=["PUT"])
@jwt_required()
def update_user(username):
    try:
        current_user = get_jwt_identity()
        if current_user != username:
            return jsonify({"message": "Accès non autorisé"}), 403

        data = request.get_json()

        app.logger.info(f"type data : {type(data)} | data : {data}")

        user = User.query.filter_by(username=username).first()
        if not user:
            return jsonify({"message": "Utilisateur non trouvé"}), 404

        for key in data.keys():
            if key not in ["lastName", "firstName", "email", "password", "pseudo"]:
                return jsonify({"message": "Mauvais paramètre fourni"}), 401

        # Mise à jour des informations de l'utilisateur
        
        if("lastName" in data.keys()):
            user.last_name = data.get("lastName", user.last_name) 
        if("firstName" in data.keys()):
            user.first_name = data.get("firstName", user.first_name)
        if("email" in data.keys()):
            user.email = data.get("email", user.email)
        if("password" in data.keys()):
            user.set_password(data.get("password", user.password))
        if("pseudo" in data.keys()):
            user.pseudo = data.get("pseudo", user.pseudo)



        db.session.commit()
        return jsonify({"message": "L'utilisation a bien été modifié"}), 200

    except Exception as e:
        return jsonify({"message": "Erreur interne du serveur", "error": str(e)}), 500
