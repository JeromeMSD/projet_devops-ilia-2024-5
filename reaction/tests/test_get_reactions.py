import pytest
import sys
import os 
import json

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'../src')))
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_get_tweet_reactions(client):
    tweet_id = 1
    response = client.get(f'/tweets/{tweet_id}/reactions')
    
    # Ajoutons des prints pour debug
    print(f"\nStatus Code: {response.status_code}")
    print(f"Response Data: {response.data}")
    if response.data:
        print(f"Response JSON: {json.loads(response.data)}")
    
    assert response.status_code == 200
    assert isinstance(response.json, list)