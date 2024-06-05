from django.test import TestCase, Client
from django.urls import reverse

class TemplateTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_index_template(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_static_files_loading(self):
        response = self.client.get(reverse('index'))
        self.assertContains(response, 'href="/static/css/styles.css"')
        self.assertContains(response, 'src="/static/img/intro.png"')
        self.assertContains(response, 'src="/static/js/scripts.js"')
