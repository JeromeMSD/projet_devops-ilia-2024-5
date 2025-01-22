from flask import Flask
from routes.blueprints_path import messages_bp
from flask_cors import CORS # type: ignore

app = Flask(__name__)
CORS(app)

# Fonction pour enregistrer les routes depuis le dossier ./routes
def load_routes():
    for bp in messages_bp:
        app.register_blueprint(bp)
       
@app.route('/')
def index():
    return 'Bienvenue sur la page d\'accueil !'
 
load_routes()



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
