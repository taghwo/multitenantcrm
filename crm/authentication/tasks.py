from celery import shared_task
from signals.senders import new_account
from account.models import Account
from notification.notifications.newusernotification import NewUserNotification

@shared_task
def new_user_job(**kwargs):
    notification = NewUserNotification(data=kwargs)
    notification.notify()

