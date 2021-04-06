from notification.basemailer import BaseMailer


class RegistrationMail(BaseMailer):

    def __init__(self, user, *args):

        self.username = user['username']
        self.fullname = user['fullname']

        super().__init__()

    def render(self):

        self.subject('Registration successful') \
            .template(['emails/registration/reg.html',
                       'emails/registration/reg.txt']) \
            .to('example@example.com') \
            .sender('example@example.com') \
            .send()

