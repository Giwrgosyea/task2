"""
Main unittest script
To run unittest python3 tests.py

"""
import unittest
from app import app


class SimpleRequestTest(unittest.TestCase):
    """
    This class is used for request based unit tests
    """
    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def test_main_page(self):
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_fib_page(self):
        response = self.app.get('/fib/12', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_health_page(self):
        response = self.app.get('/health', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main(verbosity=2)