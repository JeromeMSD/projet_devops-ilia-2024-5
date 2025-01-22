import unittest
from src.app import create_app

class TweetTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app().test_client()
        self.app.testing = True

    def test_create_tweet_success(self):
        response = self.app.post('/tweet', json={'content': 'This is a new tweet'})
        self.assertEqual(response.status_code, 201)
        data = response.get_json()
        self.assertEqual(data['message'], 'This is a new tweet')
        self.assertEqual(data['author'], 'BiduleLaCartouse')
        self.assertEqual(data['reaction']['like'], 0)
        self.assertEqual(data['reaction']['comment'], 0)
        self.assertEqual(data['reaction']['retweet'], 0)

    def test_create_tweet_invalid_input(self):
        response = self.app.post('/tweet', json={})
        self.assertEqual(response.status_code, 400)
        self.assertIn('Invalid input', response.get_data(as_text=True))

if __name__ == '__main__':
    unittest.main()