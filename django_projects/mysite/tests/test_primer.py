# mysite/tests/test_primer.py
from django.test import TestCase

class PrimerTestCase(TestCase):
    def test_index(self):
        response = self.client.get('/primer/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Hello, world. You're at the primer index.")