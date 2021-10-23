from account.models import Account
from invoice.models import Invoice
from django.dispatch import receiver
from notification.notifications.newusernotification import NewUserNotification
from notification.mailers.invoicemail import InvoiceMail
from django.db.models.signals import post_save,pre_save
from signals.senders import new_account

@receiver(new_account,sender=Account)
def send_welcome_mail(sender,**kwargs):
    notification = NewUserNotification(data=kwargs)
    notification.notify()


@receiver(post_save, sender=Invoice)
def send_invoice_mail(sender, **kwargs):
    if InvoiceMail(kwargs['invoice']):
        print("invoice sent")