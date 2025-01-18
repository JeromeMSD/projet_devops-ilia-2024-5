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

# Test pour la suppression de commentaire
def test_delete_comment(client, redis_client):
    tweet_id = "12345"
    comment_id = 1
    data = {
        "commentId": comment_id,
        "userId": "user1",
        "content": "This is a test comment"
    }

    # Ajouter un commentaire dans Redis
    redis_client.rpush(f"comments:{tweet_id}", str(data))

    # Vérifier que le commentaire est ajouté
    comments_before = redis_client.lrange(f"comments:{tweet_id}", 0, -1)
    assert len(comments_before) == 1

    # Supprimer le commentaire via l'API
    response = client.delete(f'/tweets/{tweet_id}/comments/{comment_id}')

    # Vérifier la réponse
    assert response.status_code == 200
    response_data = response.get_json()
    assert "message" in response_data
    assert response_data["message"] == "Commentaire supprimé avec succès."

    # Vérifier que le commentaire a été supprimé de Redis
    comments_after = redis_client.lrange(f"comments:{tweet_id}", 0, -1)
    assert len(comments_after) == 0
