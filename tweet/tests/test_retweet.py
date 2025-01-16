
import unittest
from src.app import create_app

class RetweetRoutesTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        self.app.config['TESTING'] = True

    # Test for valid /retweet/<tweetId>
    def test_valid_retweet(self):
        response = self.client.post('/retweet/1')  # Simulate retweeting tweet with ID 1
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['message'], 'Tweet retweeted')

    # Test for invalid tweet ID
    def test_invalid_tweet_id(self):
        response = self.client.post('/retweet/0')  # Simulate retweeting with invalid ID
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json['message'], 'Invalid tweet ID')

    # Test for non-existent tweet
    def test_tweet_not_found(self):
        response = self.client.post('/retweet/999')  # Simulate retweeting a non-existent tweet
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json['message'], 'Tweet not found')

    # Test for unsupported method
    def test_unsupported_method(self):
        response = self.client.get('/retweet/1')  # Simulate invalid GET request
        self.assertEqual(response.status_code, 405)  # 405 Method Not Allowed


if _name_ == '_main_':
    unittest.main()

