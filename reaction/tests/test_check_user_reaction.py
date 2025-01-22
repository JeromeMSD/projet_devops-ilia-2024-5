import pytest
import sys
import os
import json
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

# Test pour vérifier si un utilisateur a réagi
def test_check_user_reaction(client, redis_client):
    user_id = "user1"
    item_id = "12345"
    item_type = "tweet"  # Peut aussi être "comment"
    reaction = "like"

    # Simuler les données dans Redis
    reaction_data = {"user_id": user_id, "reaction": reaction}
    redis_client.rpush(f"reactions:{item_type}s:{item_id}", json.dumps(reaction_data))

    # Envoyer une requête GET avec les paramètres
    response = client.get(f'/reactions/check?user_id={user_id}&item_id={item_id}&item_type={item_type}&reaction={reaction}')

    # Vérifier la réponse
    assert response.status_code == 200
    response_data = response.get_json()

    # Vérifier si l'utilisateur a réagi
    assert response_data == {"has_reacted": True}
