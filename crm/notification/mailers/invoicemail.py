from notification.mailers.basemailer import BaseMailer
from modules.Util import email_sender

class InvoiceMail(BaseMailer):

    def __init__(self, invoice, *args):

        self.invoice = invoice

    def render(self):
        self.subject(f"Invoice from {self.invoice.tenant.name}") \
            .template(['emails/invoice/puritan.html',
                       'emails/invoice/puritan.txt']) \
            .to(self.invoice.tenant.business_email) \
            .sender(email_sender('support'))\
            .send()

