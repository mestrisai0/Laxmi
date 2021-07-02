
import os
from celery import Celery
from django.conf import settings
# from celery.schedules import crontab
# from apex.decoraters import *
# celery = Celery(
#     "gringotts", broker=settings.CELERY_BROKER, include=["app.tasks"]
# )
# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LaxmiIndustries.settings')

app = Celery('LaxmiIndustries')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.beat_schedule = {

    'mail': {
        'task': 'Laxmi.tasks.send_mail',
        'schedule':10,
    }
}

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')