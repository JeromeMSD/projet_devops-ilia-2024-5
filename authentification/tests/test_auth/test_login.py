import pytest
from flask import json
from models.example_model import User

def test_login_success(client, test_user):
    response = client.post('/auth/login', json={
        "username_or_email": "johndoe",
        "password": "password123"
    })
    assert response.status_code == 200
    data = json.loads(response.data)
    assert "token" in data  # Vérifie que le token est dans la réponse

def test_login_invalid_credentials(client):
    response = client.post('/auth/login', json={
        "username_or_email": "fakeuser",
        "password": "wrongpassword"
    })
    assert response.status_code == 401
    data = json.loads(response.data)
    assert data["message"] == "Nom d'utilisateur ou mot de passe incorrect"

def test_login_missing_fields(client):
    response = client.post('/auth/login', json={})
    assert response.status_code == 400
    data = json.loads(response.data)
    assert data["message"] == "Nom d'utilisateur ou mot de passe requis"
