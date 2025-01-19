import pytest
import sys
import os
import redis

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src/')))

from app import create_app

# Redis mock setup
@pytest.fixture
def redis_client():
    client = redis.Redis(host='localhost', port=6379, db=0)
    client.flushdb()  # Nettoyer la base Redis avant chaque test
    return client

# Flask test client setup
@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

# Test pour ajouter une réaction à un commentaire
def test_add_reaction(client, redis_client):
    comment_id = 1
    data = {
        "user_id": "12345",
        "reaction": "love"
    }

    # Appeler la route POST pour ajouter une réaction
    response = client.post(f'/comments/{comment_id}/reactions', json=data)

    # Vérifier la réponse de l'API
    assert response.status_code == 201
    response_data = response.get_json()
    assert "message" in response_data
    assert response_data["message"] == "Réaction ajoutée avec succès."

    # Vérifier que la réaction est stockée dans Redis
    reactions = redis_client.lrange(f"comment:{comment_id}:reactions", 0, -1)
    assert len(reactions) == 1

    # Convertir la chaîne de Redis en dictionnaire Python
    stored_reaction = eval(reactions[0].decode())

    # Vérifier les données stockées
    assert stored_reaction["user_id"] == data["user_id"]
    assert stored_reaction["reaction"] == data["reaction"]
