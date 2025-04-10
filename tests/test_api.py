import unittest
import requests

class TestAPI(unittest.TestCase):
    def test_health(self):
        response = requests.get('http://localhost:5000/health')
        self.assertEqual(response.json().get('status'), 'healthy')

if __name__ == '__main__':
    unittest.main()
