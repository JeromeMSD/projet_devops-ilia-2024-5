import pytest
from app import create_app
from unittest.mock import patch

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

@patch('services.reaction_service.get_redis_client')
def test_delete_tweet_reaction(mock_redis_client, client):
    # Simuler Redis
    mock_redis = mock_redis_client.return_value
    mock_redis.hdel.return_value = 1  # Simule la suppression réussie

    # Simuler la requête DELETE
    response = client.delete('/tweets/123/reactions/1')

    # Vérifier la réponse
    assert response.status_code == 200
    assert response.json == {"message": "Réaction supprimée avec succès."}

    # Vérifier que Redis a été appelé correctement
    mock_redis.hdel.assert_called_with("tweet:123:reactions", 1)
