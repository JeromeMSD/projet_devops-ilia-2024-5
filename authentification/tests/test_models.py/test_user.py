import pytest
from models.example_model import User
from config import db

def test_user_creation():
    user = User(
        nom="Doe",
        prenom="John",
        email="john@example.com",
        password="password123",
        username="johndoe",
        pseudo="jd"
    )
    assert user.nom == "Doe"
    assert user.prenom == "John"
    assert user.email == "john@example.com"
    assert user.username == "johndoe"
    assert user.pseudo == "jd"
    assert user.password == "password123"

def test_user_to_dict():
    user = User(
        nom="Doe",
        prenom="John",
        email="john@example.com",
        password="password123",
        username="johndoe",
        pseudo="jd"
    )
    user_dict = user.to_dict()
    assert user_dict["nom"] == "Doe"
    assert user_dict["prenom"] == "John"
    assert user_dict["email"] == "john@example.com"
    assert user_dict["username"] == "johndoe"
    assert user_dict["pseudo"] == "jd"
    assert "password" not in user_dict
