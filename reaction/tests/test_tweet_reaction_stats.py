import pytest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src/')))

from app import create_app
import redis

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

# Test pour les statistiques de réactions d'un tweet
def test_get_tweet_reaction_stats(client, redis_client):
    tweet_id = "12345"

    # Simuler les statistiques des réactions dans Redis
    redis_client.hset(f"tweet:{tweet_id}:reactions_stat", mapping={
        "like": 10,
        "love": 5,
        "haha": 2
    })

    # Envoyer une requête GET à la route
    response = client.get(f'/tweets/{tweet_id}/reactions/stats')

    # Vérifier la réponse
    assert response.status_code == 200
    response_data = response.get_json()

    # Vérifier les statistiques
    assert response_data == {
        "like": 10,
        "love": 5,
        "haha": 2
    }
