import pytest
from flask import json
from models.example_model import User

def test_register_success(client):
    response = client.post('/auth/sign_in', json={
        "nom": "Doe",
        "prenom": "John",
        "email": "john@example.com",
        "password": "password123",
        "username": "johndoe",
        "pseudo": "jd"
    })
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data["message"] == "Utilisateur créé avec succès"

def test_register_duplicate_user(client, test_user):
    response = client.post('/auth/sign_in', json={
        "nom": "Doe",
        "prenom": "Jane",
        "email": "jane@example.com",
        "password": "password123",
        "username": "johndoe",  # Nom d'utilisateur déjà pris
        "pseudo": "janejd"
    })
    assert response.status_code == 409
    data = json.loads(response.data)
    assert "Nom d'utilisateur ou email déjà utilisé" in data["message"]

def test_register_missing_fields(client):
    response = client.post('/auth/sign_in', json={
        "nom": "Doe",
        "prenom": "John"
    })
    assert response.status_code == 400
    data = json.loads(response.data)
    assert data["message"] == "Tous les champs sont obligatoires"
