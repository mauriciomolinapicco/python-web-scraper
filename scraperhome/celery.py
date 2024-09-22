import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'scraperhome.settings')

app = Celery('scraperhome')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()  #its gonna look in all apps for tasks.py

app.conf.broker_url = 'redis://localhost:6379'


# app.conf.beat_schedule = {
#     "multiply-task-crontab": {
#         "task": "multiply-two-numbers",
#         "schedule": crontab(hour=7, minute=30, day_of_week=1),
#         "args":(16,16),
#     },
#     "add-every-30-seconds": {
#         "task": "movies.tasks.add",
#         "schedule": 30.0,
#         "args": (16,16),
#     }
# }