import os
import sys

from celery.schedules import crontab

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TESTING = sys.argv[1] == 'test'
SHELL = 'shell' in sys.argv or 'shell_plus' in sys.argv

# Set DEBUG to False in production
DEBUG = True

SECRET_KEY = '&a@f(0@lrl%606smticbu20=pvribdvubk5=gjti8&n1y%bi&4'

ALLOWED_HOSTS = []
IMMUNITY
_RADIUS_FREERADIUS_ALLOWED_HOSTS = ['127.0.0.1']
IMMUNITY
_RADIUS_COA_ENABLED = True
IMMUNITY
_RADIUS_ALLOWED_MOBILE_PREFIXES = ['+44', '+39', '+237', '+595']

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    # immunity admin theme
    'immunity_utils.admin_theme',
    'immunity_users.accounts',
    # all-auth
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    # rest framework
    'rest_framework',
    'django_filters',
    # registration
    'rest_framework.authtoken',
    'dj_rest_auth',
    'dj_rest_auth.registration',
    # social login
    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.google',
    # immunity radius
    'immunity_radius',
    'immunity_users',
    # admin
    'admin_auto_filters',
    'django.contrib.admin',
    'private_storage',
    'drf_yasg',
    'django_extensions',
    'immunity2.integrations',
    'djangosaml2',
]

LOGIN_REDIRECT_URL = 'admin:index'

AUTHENTICATION_BACKENDS = (
    'immunity_users.backends.UsersAuthenticationBackend',
    'immunity_radius.saml.backends.ImmunityRadiusSaml2Backend',
    'sesame.backends.ModelBackend',
)

AUTH_USER_MODEL = 'immunity_users.User'
SITE_ID = 1

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'immunity_utils.staticfiles.DependencyFinder',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'sesame.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'djangosaml2.middleware.SamlSessionMiddleware',
]

SESSION_COOKIE_SECURE = True
SESSION_EXPIRE_AT_BROWSER_CLOSE = True
SAML_ALLOWED_HOSTS = []
SAML_USE_NAME_ID_AS_USERNAME = True
SAML_CREATE_UNKNOWN_USER = True
SAML_CONFIG = {}

ROOT_URLCONF = 'immunity2.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'OPTIONS': {
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'immunity_utils.loaders.DependencyLoader',
                'django.template.loaders.app_directories.Loader',
            ],
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'immunity_utils.admin_theme.context_processor.menu_groups',
            ],
        },
    }
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'immunity_radius.db'),
    }
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': TESTING,
    'filters': {'require_debug_true': {'()': 'django.utils.log.RequireDebugTrue'}},
    'formatters': {
        'django.server': {
            '()': 'django.utils.log.ServerFormatter',
            'format': '[{server_time}] {message}',
            'style': '{',
        }
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
        },
    },
}

if not TESTING:
    LOGGING['handlers'].update(
        {
            'django.server': {
                'level': 'DEBUG',
                'class': 'logging.StreamHandler',
                'formatter': 'django.server',
            },
        }
    )
    LOGGING['loggers'] = {
        'django': {'handlers': ['console'], 'level': 'INFO'},
        'django.server': {
            'handlers': ['django.server'],
            'level': 'INFO',
            'propagate': False,
        },
        'immunity_radius': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': False,
        },
    }

if not TESTING and SHELL:
    LOGGING['loggers'] = {
        'django.db': {
            'level': 'DEBUG',
            'handlers': ['console'],
            'propagate': False,
        },
        '': {
            # this sets root level logger to log debug and higher level
            # logs to console. All other loggers inherit settings from
            # root level logger.
            'handlers': ['console', 'django.server'],
            'level': 'DEBUG',
            'propagate': False,
        },
    }

# WARNING: for development only!
AUTH_PASSWORD_VALIDATORS = []

LANGUAGE_CODE = 'en-gb'
TIME_ZONE = 'America/Asuncion'  # used to replicate timezone related bug, do not change!
USE_I18N = True
USE_L10N = True
USE_TZ = True
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
PRIVATE_STORAGE_ROOT = os.path.join(MEDIA_ROOT, 'private')
EMAIL_PORT = '1025'
MEDIA_URL = '/media/'
STATIC_URL = '/static/'

# for development only
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

SOCIALACCOUNT_PROVIDERS = {
    'facebook': {
        'METHOD': 'oauth2',
        'SCOPE': ['email', 'public_profile'],
        'AUTH_PARAMS': {'auth_type': 'reauthenticate'},
        'INIT_PARAMS': {'cookie': True},
        'FIELDS': ['id', 'email', 'name', 'first_name', 'last_name', 'verified'],
        'VERIFIED_EMAIL': True,
    },
    'google': {'SCOPE': ['profile', 'email'], 'AUTH_PARAMS': {'access_type': 'online'}},
}

redis_host = os.getenv('REDIS_HOST', 'localhost')

IMMUNITY
_RADIUS_PASSWORD_RESET_URLS = {
    '__all__': (
        'http://localhost:8080/{organization}/password/reset/confirm/{uid}/{token}'
    ),
}

if not TESTING:
    CELERY_BROKER_URL = os.getenv('REDIS_URL', f'redis://{redis_host}/1')
else:
    IMMUNITY
_RADIUS_GROUPCHECK_ADMIN = True
    IMMUNITY
_RADIUS_GROUPREPLY_ADMIN = True
    IMMUNITY
_RADIUS_USERGROUP_ADMIN = True
    IMMUNITY
_RADIUS_USER_ADMIN_RADIUSTOKEN_INLINE = True
    CELERY_TASK_ALWAYS_EAGER = True
    CELERY_TASK_EAGER_PROPAGATES = True
    CELERY_BROKER_URL = 'memory://'

TEST_RUNNER = 'immunity_utils.tests.TimeLoggingTestRunner'

CELERY_BEAT_SCHEDULE = {
    'deactivate_expired_users': {
        'task': 'immunity_radius.tasks.cleanup_stale_radacct',
        'schedule': crontab(hour=0, minute=0),
        'args': None,
        'relative': True,
    },
    'delete_old_radiusbatch_users': {
        'task': 'immunity_radius.tasks.delete_old_radiusbatch_users',
        'schedule': crontab(hour=0, minute=10),
        'args': [365],
        'relative': True,
    },
    'cleanup_stale_radacct': {
        'task': 'immunity_radius.tasks.cleanup_stale_radacct',
        'schedule': crontab(hour=0, minute=20),
        'args': [365],
        'relative': True,
    },
    'delete_old_postauth': {
        'task': 'immunity_radius.tasks.delete_old_postauth',
        'schedule': crontab(hour=0, minute=30),
        'args': [365],
        'relative': True,
    },
    'delete_old_radacct': {
        'task': 'immunity_radius.tasks.delete_old_radacct',
        'schedule': crontab(hour=0, minute=40),
        'args': [365],
        'relative': True,
    },
    'unverify_inactive_users': {
        'task': 'immunity_radius.tasks.unverify_inactive_users',
        'schedule': crontab(hour=1, minute=30),
        'relative': True,
    },
    'delete_inactive_users': {
        'task': 'immunity_radius.tasks.delete_inactive_users',
        'schedule': crontab(hour=1, minute=50),
        'relative': True,
    },
}

SENDSMS_BACKEND = 'sendsms.backends.console.SmsBackend'
IMMUNITY
_RADIUS_EXTRA_NAS_TYPES = (('cisco', 'Cisco Router'),)

REST_AUTH = {
    'SESSION_LOGIN': False,
    'PASSWORD_RESET_SERIALIZER': 'immunity_radius.api.serializers.PasswordResetSerializer',
    'REGISTER_SERIALIZER': 'immunity_radius.api.serializers.RegisterSerializer',
}

ACCOUNT_EMAIL_CONFIRMATION_ANONYMOUS_REDIRECT_URL = 'email_confirmation_success'
ACCOUNT_EMAIL_CONFIRMATION_AUTHENTICATED_REDIRECT_URL = 'email_confirmation_success'

# IMMUNITY
_RADIUS_PASSWORD_RESET_URLS = {
#     # use the uuid because the slug can change
#     # 'dabbd57a-11ca-4277-8dbb-ad21057b5ecd': 'https://org.com/{organization}/password/reset/confirm/{uid}/{token}',
#     # fallback in case the specific org page is not defined
#     '__all__': 'https://example.com/{{organization}/password/reset/confirm/{uid}/{token}',
# }

if TESTING:
    IMMUNITY
_RADIUS_SMS_TOKEN_MAX_USER_DAILY = 3
    IMMUNITY
_RADIUS_SMS_TOKEN_MAX_ATTEMPTS = 3
    IMMUNITY
_RADIUS_SMS_TOKEN_MAX_IP_DAILY = 4
    SENDSMS_BACKEND = 'sendsms.backends.dummy.SmsBackend'
else:
    IMMUNITY
_RADIUS_SMS_TOKEN_MAX_USER_DAILY = 10

IMMUNITY
_USERS_AUTH_API = True

if os.environ.get('SAMPLE_APP', False):
    INSTALLED_APPS.remove('immunity_radius')
    INSTALLED_APPS.remove('immunity_users')
    INSTALLED_APPS.append('immunity2.sample_radius')
    INSTALLED_APPS.append('immunity2.sample_users')
    EXTENDED_APPS = ('immunity_radius', 'immunity_users')
    AUTH_USER_MODEL = 'sample_users.User'
    IMMUNITY
_USERS_GROUP_MODEL = 'sample_users.Group'
    IMMUNITY
_USERS_ORGANIZATION_MODEL = 'sample_users.Organization'
    IMMUNITY
_USERS_ORGANIZATIONUSER_MODEL = 'sample_users.OrganizationUser'
    IMMUNITY
_USERS_ORGANIZATIONOWNER_MODEL = 'sample_users.OrganizationOwner'
    IMMUNITY
_USERS_ORGANIZATIONINVITATION_MODEL = 'sample_users.OrganizationInvitation'
    IMMUNITY
_RADIUS_RADIUSREPLY_MODEL = 'sample_radius.RadiusReply'
    IMMUNITY
_RADIUS_RADIUSGROUPREPLY_MODEL = 'sample_radius.RadiusGroupReply'
    IMMUNITY
_RADIUS_RADIUSCHECK_MODEL = 'sample_radius.RadiusCheck'
    IMMUNITY
_RADIUS_RADIUSGROUPCHECK_MODEL = 'sample_radius.RadiusGroupCheck'
    IMMUNITY
_RADIUS_RADIUSACCOUNTING_MODEL = 'sample_radius.RadiusAccounting'
    IMMUNITY
_RADIUS_NAS_MODEL = 'sample_radius.Nas'
    IMMUNITY
_RADIUS_RADIUSUSERGROUP_MODEL = 'sample_radius.RadiusUserGroup'
    IMMUNITY
_RADIUS_REGISTEREDUSER_MODEL = 'sample_radius.RadiusUserGroup'
    IMMUNITY
_RADIUS_RADIUSPOSTAUTH_MODEL = 'sample_radius.RadiusPostAuth'
    IMMUNITY
_RADIUS_RADIUSBATCH_MODEL = 'sample_radius.RadiusBatch'
    IMMUNITY
_RADIUS_RADIUSGROUP_MODEL = 'sample_radius.RadiusGroup'
    IMMUNITY
_RADIUS_RADIUSTOKEN_MODEL = 'sample_radius.RadiusToken'
    IMMUNITY
_RADIUS_PHONETOKEN_MODEL = 'sample_radius.PhoneToken'
    IMMUNITY
_RADIUS_REGISTEREDUSER_MODEL = 'sample_radius.RegisteredUser'
    IMMUNITY
_RADIUS_ORGANIZATIONRADIUSSETTINGS_MODEL = (
        'sample_radius.OrganizationRadiusSettings'
    )
    # Rename sample_app database
    DATABASES['default']['NAME'] = os.path.join(BASE_DIR, 'sample_radius.db')
    CELERY_IMPORTS = ('immunity_radius.tasks',)

if os.environ.get('SAMPLE_APP', False) and TESTING:
    # Required for immunity-users tests
    IMMUNITY
_ORGANIZATION_USER_ADMIN = True
    IMMUNITY
_ORGANIZATION_OWNER_ADMIN = True
    IMMUNITY
_USERS_AUTH_API = True

# CORS headers, useful during development and testing
try:
    import corsheaders  # noqa

    INSTALLED_APPS.append('corsheaders')
    MIDDLEWARE.insert(
        MIDDLEWARE.index('django.middleware.common.CommonMiddleware'),
        'corsheaders.middleware.CorsMiddleware',
    )
    # WARNING: for development only!
    CORS_ORIGIN_ALLOW_ALL = True
except ImportError:
    pass

# local settings must be imported before test runner otherwise they'll be ignored
try:
    from .local_settings import *
except ImportError:
    pass
