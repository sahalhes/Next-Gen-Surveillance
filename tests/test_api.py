import unittest
from backend.app import app

class TestAPI(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_index(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Welcome to Next Gen Surveillance', response.data.decode())

    def test_track(self):
        response = self.app.post('/track', json={'culprit_id': 123})
        self.assertEqual(response.status_code, 200)
        self.assertIn('Tracking started', response.data.decode())

if __name__ == '__main__':
    unittest.main()
