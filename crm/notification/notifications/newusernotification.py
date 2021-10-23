from notification.mailers.registrationmail import RegistrationMail
from notification.sms.nexmo import NexmoSMS
from notification.notifications.noficationinterface import NoficationInterface


class NewUserNotification(NoficationInterface):
    def __init__(self, *args, **kwargs) -> None:
        self.kwargs = kwargs['data']

    def via(self):
        return ['mail', 'sms']

    def to_mail(self):
        mailer = RegistrationMail(self.kwargs['user'])
        return  mailer.render()

    def to_sms(self):
        sms = NexmoSMS(self.kwargs['user'])
        return sms.send()