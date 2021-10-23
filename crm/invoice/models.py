from contact.models import Contact
from django.db.models.deletion import CASCADE, SET_NULL
from django.utils.timezone import now
from account.models import Account
from invoicetemplate.models import InvoiceTemplate

import uuid
from django.db import models
from tenant.models import Tenant
class Invoice(models.Model):
     uuid = models.UUIDField(default=uuid.uuid4, editable=False)
     link = models.URLField(null=True,blank=True)
     due_date = models.DateTimeField()
     number = models.IntegerField(null=False,blank=False)
     header = models.CharField(max_length=500,null=True, blank=True)
     issued_date = models.DateField()
     extra_notes = models.CharField(max_length=1000,null=True, blank=True)
     items = models.JSONField(null=False,blank=False)
     status = models.CharField(max_length=50, default='pending', choices=(('pending','pending'),('cleared','cleared'),('canceled','canceled')))
     is_drafted = models.BooleanField(default=1)
     sub_total = models.IntegerField(null=True,blank=True)
     tax = models.IntegerField(null=True,blank=True)
     total = models.IntegerField(null=False,blank=False)
     updated_at = models.DateTimeField(default=now)
     tenant = models.ForeignKey(Tenant, related_name='tenantinvoices',null=True,  on_delete=CASCADE)
     template = models.ForeignKey(InvoiceTemplate, related_name='invoicetemplate',null=True,  on_delete=SET_NULL)
     contact = models.ForeignKey(Contact, related_name='contactinvoices',null=True, on_delete=CASCADE)
     created_by = models.ForeignKey(Account, related_name="createdinvoice",null=True, blank=True, on_delete=SET_NULL)
     updated_by = models.ForeignKey(Account, related_name="updatedinvoices",null=True,  blank=True, on_delete=SET_NULL)

     class meta:
         verbose_name_plural = ['invoices']

     def __str__(self):
         return self.link

     @property
     def total_to_string(self):
         return "{:,.2f}".format(self.total/1000)
     @property
     def sub_total_to_string(self):
         return "{:,.2f}".format(self.sub_total/1000)

     def save(self,*args,**kwargs):
        self.fee = self.total*1000
        self.sub_total = self.sub_total*1000
        super().save(*args,**kwargs)
