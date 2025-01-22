import pytest
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import app, db
from models.example_model import User

# Fixture de l'application Flask
@pytest.fixture(scope="module")
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.test_client() as client:
        with app.app_context():
            db.create_all()  # Création de la base de données en mémoire
        yield client
        db.session.remove()
        db.drop_all()

# Fixture d'un utilisateur pour les tests
@pytest.fixture
def test_user():
    user = User(
        nom="Doe",
        prenom="John",
        email="john@example.com",
        password="password123",
        username="johndoe",
        pseudo="jd"
    )
    db.session.add(user)
    db.session.commit()
    return user
