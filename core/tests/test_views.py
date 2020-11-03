from django.test import TestCase, Client


class IndexViewTestCase(TestCase):
    def setUp(self):
        # Client simula o navegador
        self.client = Client()
        self.response_url_index = self.client.get('/')

    def tearDown(self):
        pass

    def test_status_code(self):
        self.assertEqual(self.response_url_index.status_code, 200)

    def test_template_used(self):
        self.assertTemplateUsed(self.response_url_index, 'index.html')
