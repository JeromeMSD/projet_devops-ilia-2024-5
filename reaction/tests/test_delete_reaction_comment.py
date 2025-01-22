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
    client.flushdb()  # Clean Redis before each test
    yield client
    client.flushdb()  # Clean up after each test

def test_delete_reaction_comment(client, redis_client):
    # Set up test data
    comment_id = "67890"  # Exemple d'ID de commentaire
    reaction_id = "12345"  # Utilisation d'un entier pour correspondre au modèle
    reaction_type = "like"

    # Ajouter une liste de réactions à Redis associée au commentaire
    reactions = [
        {
            "reaction_id": reaction_id,
            "user_id": "user123",
            "reaction": reaction_type
        },
        {
            "reaction_id": "12346",
            "user_id": "user456",
            "reaction": "love"
        }
    ]
    redis_client.set(f"comment:{comment_id}:reactions", str(reactions))

    # Ajouter des statistiques des réactions au commentaire
    reactions_stat = {
        "like": 10,
        "love": 5,
        "haha": 2,
        "sad": 1
    }
    redis_client.set(f"comment:{comment_id}:reactions_stat", str(reactions_stat))

    # Simuler la requête DELETE
    response = client.delete(f'/comments/{comment_id}/reactions/{reaction_id}')

    # Vérifier la réponse
    assert response.status_code == 200

    # Vérifier que la réaction a été supprimée de Redis
    updated_reactions = eval(redis_client.get(f"comment:{comment_id}:reactions"))
    assert len(updated_reactions) == 1  # Une seule réaction doit rester
    assert all(r["reaction_id"] != reaction_id for r in updated_reactions)  # Aucune réaction avec cet ID

    # Vérifier que les statistiques des réactions ont été mises à jour correctement
    updated_reactions_stat = eval(redis_client.get(f"comment:{comment_id}:reactions_stat"))
    assert updated_reactions_stat["like"] == 9  # Le compteur "like" doit être décrémenté

    # Vérifier que les autres statistiques restent inchangées
    assert updated_reactions_stat["love"] == 5
    assert updated_reactions_stat["haha"] == 2
    assert updated_reactions_stat["sad"] == 1
