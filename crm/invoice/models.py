from crm.contact.models import Contact
from crm.transaction.models import Transaction
from django.db.models.deletion import SET_NULL
from django.utils.timezone import now
from account.models import Account

import uuid
from django.db import models
from tenant.models import Tenant
class Invoice(models.Model):
     uuid = models.UUIDField(default=uuid.uuid4, editable=False)
     title = models.CharField(null=False,blank=False,max_length=500,default="puritan")
     total_amount = models.IntegerField(null=True,blank=True)
     created_at = models.DateTimeField(default=now)
     updated_at = models.DateTimeField(default=now)
     tenant = models.ForeignKey(Tenant, related_name='tenantinvoices',null=True, default=None, on_delete=SET_NULL)
     contact = models.ForeignKey(Contact, related_name='contactinvoices',null=True, default=None, on_delete=SET_NULL)
     transaction = models.ForeignKey(Transaction, related_name='transactioninvoices',null=True, default=None, on_delete=SET_NULL)
     created_by = models.ForeignKey(Account, related_name="createdinvoice",null=True, default=None, blank=True, on_delete=SET_NULL)
     updated_by = models.ForeignKey(Account, related_name="updatedtransactions",null=True, default=None, blank=True, on_delete=SET_NULL)

     class meta:
         ordering = ['name']
         verbose_name_plural = ['invoice']

     def __str__(self):
         return self.name

