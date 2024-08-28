import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'scraperhome.settings')

app = Celery('scraperhome')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()  #its gonna look in all apps for tasks.py

app.conf.broker_url = 'redis://localhost:6379'
