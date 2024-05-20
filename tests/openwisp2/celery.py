import os

from celery import Celery

# Replace 'immunity2.settings' with path to your settings.py should be relative
# from the location where celery command is executed.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'immunity2.settings')

app = Celery('immunity2')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
