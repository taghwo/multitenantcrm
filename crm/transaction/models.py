from django.db.models.deletion import SET_NULL
from django.utils.timezone import now
import uuid
from django.db import models
from tenant.models import Tenant
from account.models import Account
from contact.models import Contact
from company.models import Company
class Transaction(models.Model):
     uuid = models.UUIDField(default=uuid.uuid4, editable=False)
     name = models.CharField(null=False,blank=False,max_length=500)
     detail = models.TextField(null=True,blank=True,max_length=3000)
     fee = models.BigIntegerField(null=True,blank=True,default=0.00)
     status = models.CharField(choices=[('pending','pending'),('cleared','cleared')],blank=True,null=True, default="pending",max_length=200)
     type = models.CharField(null=False, blank=False, choices=[('onetime','onetime'),('re-occuring','re-occuring')],default="onetime", max_length=250)
     created_at = models.DateTimeField(default=now)
     updated_at = models.DateTimeField(default=now)
     tenant = models.ForeignKey(Tenant, related_name='transactions',null=True, default=None, on_delete=SET_NULL)
     contact = models.ForeignKey(Contact, related_name='transactions',null=True, default=None, on_delete=SET_NULL)
     company = models.ForeignKey(Company, related_name='transactions',null=True, default=None, on_delete=SET_NULL)
     created_by = models.ForeignKey(Account, related_name="createdtransactions",null=True, default=None, blank=True, on_delete=SET_NULL)
     updated_by = models.ForeignKey(Account, related_name="updatedtransactions",null=True, default=None, blank=True, on_delete=SET_NULL)
     custom_data = models.JSONField(null=True,blank=True)

     class meta:
         ordering = ['name']
         verbose_name_plural = ['transactions']

     def __str__(self):
         return self.name

     @property
     def fee_to_string(self):
         return "{:,.2f}".format(self.fee/1000)
     def save(self,*args,**kwargs):
        self.fee = self.fee*1000
        super().save(*args,**kwargs)
