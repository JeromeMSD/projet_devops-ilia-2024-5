import pytest
import json
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src/')))

from app import create_app
from db.redis_client import get_redis_client

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

@pytest.fixture
def redis_client():
    client = get_redis_client()
    client.flushdb()  # Nettoyer la base Redis avant chaque test
    yield client
    client.flushdb()  # Nettoyer après chaque test

def test_delete_tweet_reaction(client, redis_client):
    # Set up test data
    tweet_id = "123"
    reaction_id = "15166"  # Utilisation d'un entier pour correspondre au modèle
    reaction_type = "like"

    # Ajouter une liste de réactions à Redis
    reactions = [
        {
            "reaction_id": reaction_id,
            "user_id": "user123",
            "reaction": reaction_type,
            "created_at": "2025-01-10T10:05:00Z"
        },
        {
            "reaction_id": "15167",
            "user_id": "user456",
            "reaction": "love",
            "created_at": "2025-01-10T10:10:00Z"
        }
    ]
    redis_client.set(f"tweet:{tweet_id}:reactions", str(reactions))

    # Initialiser reactions_stat avec des compteurs
    reactions_stat = {
        "like": 20,
        "love": 5,
        "haha": 2,
        "sad": 1
    }
    redis_client.set(f"tweet:{tweet_id}:reactions_stat", str(reactions_stat))

    # Simuler la requête DELETE
    response = client.delete(f'/tweets/{tweet_id}/reactions/{reaction_id}')

    # Vérifier la réponse
    assert response.status_code == 200

    # Vérifier que la réaction a été supprimée de Redis
    updated_reactions = eval(redis_client.get(f"tweet:{tweet_id}:reactions"))
    assert len(updated_reactions) == 1  # Une seule réaction doit rester
    assert all(r["reaction_id"] != reaction_id for r in updated_reactions)  # Aucune réaction avec cet ID

    # Vérifier que le compteur dans reactions_stat a été mis à jour correctement
    updated_reactions_stat = eval(redis_client.get(f"tweet:{tweet_id}:reactions_stat"))
    assert updated_reactions_stat["like"] == 19  # Le compteur "like" doit être décrémenté

    # Vérifier que les autres compteurs restent inchangés
    assert updated_reactions_stat["love"] == 5
    assert updated_reactions_stat["haha"] == 2
    assert updated_reactions_stat["sad"] == 1

