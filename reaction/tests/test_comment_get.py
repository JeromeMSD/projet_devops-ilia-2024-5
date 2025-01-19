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

# Test pour la récupération des commentaires
def test_get_comments(client, redis_client):
    tweet_id = "12345"
    
    # Ajouter un commentaire à Redis pour ce tweet
    comment_data = {
        "userId": "user1",
        "content": "This is a test comment"
    }
    comment_data2 = {
        "userId": "user1",
        "content": "This is a test comment"
    }

    client.post(f'/tweets/{tweet_id}/comments', json=comment_data)
    client.post(f'/tweets/{tweet_id}/comments', json=comment_data2)

    # Envoyer une requête GET pour récupérer les commentaires
    response = client.get(f'/tweets/{tweet_id}/comments')

    # Vérifier la réponse
    assert response.status_code == 200
    response_data = response.get_json()

    # Vérifier la structure de la réponse
    assert isinstance(response_data, list)  # La réponse doit être une liste
    assert len(response_data) == 2  # Un seul commentaire doit être présent
    assert "commentId" in response_data[0]
    assert "userId" in response_data[0]
    assert "content" in response_data[0]
    assert "created_at" in response_data[0]
