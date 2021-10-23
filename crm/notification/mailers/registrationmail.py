from notification.mailers.basemailer import BaseMailer
from modules.Util import email_sender

class RegistrationMail(BaseMailer):

    def __init__(self, user, *args):
        self.username = user['username']
        self.email = user['email']
        self.fullname = user['fullname']

    def render(self):
        self.subject('Registration successful') \
            .template(['emails/registration/reg.html',
                       'emails/registration/reg.txt']) \
            .to(self.email) \
            .sender(email_sender('support')) \
            .send()

