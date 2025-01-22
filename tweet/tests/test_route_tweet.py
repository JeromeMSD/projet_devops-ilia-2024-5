import unittest
from src.app import create_app

class TweetTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app().test_client()
        self.app.testing = True

    def test_create_tweet(self):
        response = self.app.post('/tweet', json={'content': 'This is a new tweet'})
        self.assertEqual(response.status_code, 200)
        self.assertIn('Tweet created successfully', response.get_data(as_text=True))

if __name__ == '__main__':
    unittest.main()