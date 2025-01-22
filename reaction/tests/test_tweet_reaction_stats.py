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

# Test pour les statistiques de réactions d'un tweet
def test_get_tweet_reaction_stats(client, redis_client):
    tweet_id = "12345"

    # Simuler les réactions dans Redis
    redis_client.rpush(f"reactions:tweets:{tweet_id}", 
        '{"user_id": "1", "reaction": "like"}',
        '{"user_id": "2", "reaction": "love"}',
        '{"user_id": "3", "reaction": "like"}',
        '{"user_id": "4", "reaction": "haha"}',
        '{"user_id": "5", "reaction": "like"}',
        '{"user_id": "6", "reaction": "love"}',
        '{"user_id": "7", "reaction": "haha"}',
        '{"user_id": "8", "reaction": "like"}',
        '{"user_id": "9", "reaction": "love"}',
        '{"user_id": "10", "reaction": "like"}'
    )

    # Envoyer une requête GET à la route
    response = client.get(f'/tweets/{tweet_id}/reactions/stats')

    # Vérifier la réponse
    assert response.status_code == 200
    response_data = response.get_json()

    # Vérifier les statistiques
    assert response_data == {
        "like": 5,
        "love": 3,
        "haha": 2
    }
