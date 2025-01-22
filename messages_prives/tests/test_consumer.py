import pytest
import redis
import sys
import os

from src.consumer import Consumer

@pytest.fixture
def redis_client():
    client = redis.StrictRedis(host='localhost', port=6379, db=0)
    yield client
    client.flushdb()

@pytest.fixture
def consumer(redis_client):
    return Consumer(redis_client)

def test_consumer_process_message(consumer, redis_client):
    # Arrange
    message = {"key": "value"}
    redis_client.set('test_key', 'test_value')

    # Act
    consumer.process_message(message)

    # Assert
    assert redis_client.get('test_key') == b'test_value'

def test_consumer_handles_empty_message(consumer):
    # Arrange
    message = {}

    # Act
    result = consumer.process_message(message)

    # Assert
    assert result is None 