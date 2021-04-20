from django.db.models.deletion import SET_NULL
from django.utils.timezone import now
import uuid
from django.db import models
from tenant.models import Tenant
class InvoiceTemplate(models.Model):
     uuid = models.UUIDField(default=uuid.uuid4, editable=False)
     name = models.CharField(null=False,blank=False,max_length=500,default="puritan")
     cover = models.FileField(upload_to='invoicetemplatecover/', null=False, blank=False,default="invoicetemplatecover/default.jpg")
     created_at = models.DateTimeField(default=now)
     updated_at = models.DateTimeField(default=now)
     tenant = models.ForeignKey(Tenant, related_name='invoicetemplates',null=True, default=None, on_delete=SET_NULL)

     class meta:
         ordering = ['name']
         verbose_name_plural = ['invoicetemplates']

     def __str__(self):
         return self.name

