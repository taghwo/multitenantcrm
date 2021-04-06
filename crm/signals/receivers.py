from account.models import Account
from django.dispatch import receiver
from notification.registrationmail import RegistrationMail
from django.db.models.signals import post_save,pre_save
from signals.senders import new_account

@receiver(new_account,sender=Account)
def send_welcome_mail(sender,**kwargs):
    if RegistrationMail(kwargs['user']):
        print('sent mail')


