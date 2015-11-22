import unittest
from django.test import Client

class HomeTest(unittest.TestCase):
    def setUp(self):
        self.client = Client()

    def test_details(self):
        response = self.client.get('/home/')
        self.assertIn(response.status_code, [200,301,303])
        self.assertEqual(response.context['home_name'], 'lqe.home')
