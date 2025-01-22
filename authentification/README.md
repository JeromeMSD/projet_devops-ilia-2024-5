# Authentification 

## Introduction
Ce microservice gère la partie authentification de l'application, incluant la gestion des utilisateurs, des sessions et des tokens JWT. Il garantit une sécurité renforcée pour l'accès aux API et implémente des bonnes pratiques telles que le hachage des mots de passe et la gestion des autorisations.

## Fonctionnalités principales
- **Inscription utilisateur** : Création d'un nouveau compte utilisateur.
- **Connexion** : Authentification avec email et mot de passe, génération d'un token JWT.
- **Déconnexion** : Invalidation des sessions actives.
- **Rafraîchissement de token** : Renouvellement des tokens expirés via un token de rafraîchissement sécurisé.
- **Gestion des autorisations** : Vérification des rôles et permissions des utilisateurs pour l'accès à certaines routes.

## Architecture
 Voici les composants principaux :

```

├── src/
│   ├── models/
│   ├── __init__.py
│   ├── config.py
│   ├── main.py        # Point d'entrée de l'application.
│   ├── utils.py       # Fonctions utilitaires (hachage, vérification des tokens).
│   ├── routes.py
├── tests/
│   ├── truc.txt
├── requirements.txt
├── docker-compose.yaml
├── swagger.yaml        # Documentation des routes.
├── Dockerfile          # Conteneurisation du microservice.
└── README.md           # Documentation.
```

## Installation

### Installation locale
1. Clonez le dépôt :
   ```bash
   git clone https://github.com/JeromeMSD/projet_devops-ilia-2024-5.git
   cd projet_devops-ilia-2024-5/nom-microservice
   ```

2. Installez les dépendances :
   ```bash
   pip install -r requirements.txt
   ```

3. Configurez les variables d'environnement dans un fichier `.env` :
   ```env
   SECRET_KEY=changeme
   DATABASE_URL=sqlite:///auth.db
   JWT_EXPIRATION_TIME=3600
   ```

4. Lancez le service :
   ```bash
   python src/main.py
   ```

### Conteneurisation avec Docker
1. Construisez l'image Docker :
   ```bash
   docker build -t europe-west1-docker.pkg.dev/polytech-dijon/polytech-dijon/ms-auth:1.0 .
   ```

2. Exécutez le conteneur :
   ```bash
   docker run -d -p 8000:8000 --env-file .env europe-west1-docker.pkg.dev/polytech-dijon/polytech-dijon/ms-auth:1.0
   ```

## Documentation API

### Swagger
La documentation complète de l'API est disponible dans le fichier `swagger.yaml`. Vous pouvez visualiser cette documentation via [Swagger Editor](https://editor.swagger.io/).


## Tests
Des tests unitaires et fonctionnels sont disponibles pour valider les fonctionnalités d'authentification.

### Exécution des tests
1. Installez `pytest` :
   ```bash
   pip install pytest
   ```

2. Lancez les tests :
   ```bash
   pytest tests/
   ```

## CI/CD
Une GitHub Action est configurée pour :
- Lancer les tests automatiquement sur chaque pull request.
- Construire et déployer l'image Docker sur le registre Artifact Registry.

## Sécurité
- Les mots de passe sont hachés avec bcrypt.
- Les tokens JWT sont signés avec une clé secrète.
- Les routes sensibles sont protégées par des middlewares de vérification.
