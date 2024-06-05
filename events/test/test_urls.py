from django.test import SimpleTestCase, override_settings
from django.urls import reverse, resolve
from django.conf import settings
from django.core.files.uploadedfile import SimpleUploadedFile
from events.views import index

class TestUrls(SimpleTestCase):

    def test_index_url_is_resolved(self):
        url = reverse('index')
        self.assertEqual(resolve(url).func, index)

    @override_settings(DEBUG=True)
    def test_media_url_serving_in_debug_mode(self):
        # Override settings to simulate DEBUG=True
        url = settings.MEDIA_URL + 'dummyfile.txt'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)  # Expecting 404 as the file doesn't exist

    @override_settings(DEBUG=False)
    def test_media_url_not_serving_in_production(self):
        # Override settings to simulate DEBUG=False
        url = settings.MEDIA_URL + 'dummyfile.txt'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)  # Expecting 404 since serving media files in production is not configured

    @override_settings(DEBUG=True)
    def test_static_files_serving_in_debug_mode(self):
        url = settings.STATIC_URL + 'dummyfile.css'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)  # Expecting 404 as the file doesn't exist

