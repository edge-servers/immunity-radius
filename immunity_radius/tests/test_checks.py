from unittest.mock import patch

from django.test import TestCase

from immunity_radius import checks


class TestChecks(TestCase):
    @patch('immunity_radius.settings.SOCIAL_REGISTRATION_CONFIGURED', False)
    def test_check_social_registration_enabled(self):
        with patch('immunity_radius.settings.SOCIAL_REGISTRATION_ENABLED', False):
            error_list = checks.check_social_registration_enabled(None)
            self.assertEqual(len(error_list), 0)

        with patch('immunity_radius.settings.SOCIAL_REGISTRATION_ENABLED', True):
            error_list = checks.check_social_registration_enabled(None)
            self.assertEqual(len(error_list), 1)
            error = error_list.pop()
            self.assertEqual(error.msg, 'Improperly Configured')
            self.assertIn('OPENWISP_RADIUS_SOCIAL_REGISTRATION_ENABLED', error.hint)

    @patch('immunity_radius.settings.SAML_REGISTRATION_CONFIGURED', False)
    def test_check_saml_registration_enabled(self):
        with patch('immunity_radius.settings.SAML_REGISTRATION_ENABLED', False):
            error_list = checks.check_saml_registration_enabled(None)
            self.assertEqual(len(error_list), 0)

        with patch('immunity_radius.settings.SAML_REGISTRATION_ENABLED', True):
            error_list = checks.check_saml_registration_enabled(None)
            self.assertEqual(len(error_list), 1)
            error = error_list.pop()
            self.assertEqual(error.msg, 'Improperly Configured')
            self.assertIn('OPENWISP_RADIUS_SAML_REGISTRATION_ENABLED', error.hint)
