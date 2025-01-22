import pytest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src/')))
from db.redis_client import get_redis_client

from app import create_app
import redis

# Redis mock setup
@pytest.fixture
def redis_client():
    client = get_redis_client()
    client.flushdb()  # Nettoyer la base Redis avant chaque test
    return client

# Flask test client setup
@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

# Test pour les statistiques de réactions d'un commentaire
def test_get_comment_reaction_stats(client, redis_client):
    comment_id = "67890"

    # Simuler les statistiques des réactions dans Redis
    redis_client.rpush(f"reactions:comments:{comment_id}", *[
        '{"reaction": "like"}',
        '{"reaction": "like"}',
        '{"reaction": "like"}',
        '{"reaction": "love"}',
        '{"reaction": "angry"}',
        '{"reaction": "angry"}'
    ])

    # Envoyer une requête GET à la route
    response = client.get(f'/comments/{comment_id}/reactions/stats')

    # Vérifier la réponse
    assert response.status_code == 200
    response_data = response.get_json()

    # Vérifier les statistiques
    assert response_data == {
        "like": 3,
        "love": 1,
        "angry": 2
    }
