from notification.sms.basesms import BaseSMS

class NexmoSMS(BaseSMS):
    def __init__(self, user):
        self.phone_number = user['fullname']
        self.username = user['username']

    def send(self):
        try:
            pass
        except:
            pass

    def __get_body(self):
        return f"Hello dear {self.username}, Your account successfully created"