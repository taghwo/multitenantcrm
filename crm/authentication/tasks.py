from celery import shared_task
from celery.decorators import periodic_task
from celery.schedules import crontab
from notification.notifications.newusernotification import NewUserNotification
import time

@shared_task
def new_user_job(**kwargs):
    time.sleep(20)
    notification = NewUserNotification(data=kwargs)
    notification.notify()

