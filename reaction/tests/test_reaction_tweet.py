import pytest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from app import create_app

@pytest.fixture
def client():
    """
    Fixture pour configurer un client de test Flask.
    """
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_add_reaction(client):
    # ID du tweet
    tweet_id = 1

    # Corps de la requête
    reaction_data = {
        "userId": "12345",
        "reaction": "like"
    }

    # Appeler la route POST pour ajouter une réaction
    response = client.post(f'/tweets/{tweet_id}/reactions', json=reaction_data)

    # Vérifier le succès de l'ajout
    assert response.status_code == 201
    assert response.json.get("message") == "Réaction ajoutée avec succès."
