import unittest
from django.conf import settings


class TestSettings(unittest.TestCase):

    def test_secret_key(self):
        self.assertTrue(settings.SECRET_KEY, "SECRET_KEY is not set")

    def test_debug(self):
        self.assertTrue(settings.DEBUG, "DEBUG should be True for development")

    def test_allowed_hosts(self):
        self.assertIn('*', settings.ALLOWED_HOSTS, "ALLOWED_HOSTS should contain '*' for development")

    def test_installed_apps(self):
        required_apps = [
            'django.contrib.admin',
            'django.contrib.auth',
            'django.contrib.contenttypes',
            'django.contrib.sessions',
            'django.contrib.messages',
            'django.contrib.staticfiles',
            'events'
        ]
        for app in required_apps:
            self.assertIn(app, settings.INSTALLED_APPS, f"{app} should be in INSTALLED_APPS")

    def test_middleware(self):
        required_middleware = [
            'django.middleware.security.SecurityMiddleware',
            'django.contrib.sessions.middleware.SessionMiddleware',
            'django.middleware.common.CommonMiddleware',
            'django.middleware.csrf.CsrfViewMiddleware',
            'django.contrib.auth.middleware.AuthenticationMiddleware',
            'django.contrib.messages.middleware.MessageMiddleware',
            'django.middleware.clickjacking.XFrameOptionsMiddleware',
        ]
        for mw in required_middleware:
            self.assertIn(mw, settings.MIDDLEWARE, f"{mw} should be in MIDDLEWARE")

    def test_templates(self):
        self.assertTrue(settings.TEMPLATES, "TEMPLATES is not configured")
        self.assertTrue(settings.TEMPLATES[0]['DIRS'], "TEMPLATES DIRS should include paths")
        self.assertIn(str(settings.BASE_DIR / 'events/templates'), settings.TEMPLATES[0]['DIRS'],
                      "Templates directory for events should be set")

    def test_databases(self):
        self.assertIn('default', settings.DATABASES, "Default database should be configured")
        self.assertEqual(settings.DATABASES['default']['ENGINE'], 'django.db.backends.sqlite3',
                         "Default database engine should be sqlite3")
        self.assertEqual(settings.DATABASES['default']['NAME'], str(settings.BASE_DIR / 'db.sqlite3'),
                         "Default database name should be 'db.sqlite3'")

    def test_auth_password_validators(self):
        required_validators = [
            'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
            'django.contrib.auth.password_validation.MinimumLengthValidator',
            'django.contrib.auth.password_validation.CommonPasswordValidator',
            'django.contrib.auth.password_validation.NumericPasswordValidator',
        ]
        for validator in required_validators:
            self.assertIn(validator, [v['NAME'] for v in settings.AUTH_PASSWORD_VALIDATORS],
                          f"{validator} should be in AUTH_PASSWORD_VALIDATORS")

    def test_language_code(self):
        self.assertEqual(settings.LANGUAGE_CODE, 'en-us', "LANGUAGE_CODE should be 'en-us'")

    def test_time_zone(self):
        self.assertEqual(settings.TIME_ZONE, 'UTC', "TIME_ZONE should be 'UTC'")

    def test_use_i18n(self):
        self.assertTrue(settings.USE_I18N, "USE_I18N should be True")

    def test_use_tz(self):
        self.assertTrue(settings.USE_TZ, "USE_TZ should be True")

    def test_static_url(self):
        self.assertEqual(settings.STATIC_URL, '/static/', "STATIC_URL should be '/static/'")

    def test_staticfiles_dirs(self):
        self.assertIn(str(settings.BASE_DIR / 'static'), settings.STATICFILES_DIRS,
                      "STATICFILES_DIRS should include the 'static' directory")

    def test_default_auto_field(self):
        self.assertEqual(settings.DEFAULT_AUTO_FIELD, 'django.db.models.BigAutoField',
                         "DEFAULT_AUTO_FIELD should be 'django.db.models.BigAutoField'")


if __name__ == '__main__':
    unittest.main()
