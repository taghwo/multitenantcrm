from django.db.models.deletion import SET_NULL
from django.utils.timezone import now
from django.db import models
from tenant.models import Tenant

class Type(models.Model):
     name = models.CharField(null=False,blank=False,max_length=100)
     created_at = models.DateTimeField(default=now)
     updated_at = models.DateTimeField(default=now)
     tenant = models.ForeignKey(Tenant, related_name='types',null=True,default=None, on_delete=SET_NULL)

     class meta:
         ordering = ['name']
         verbose_name_plural = ['types']

     def __str__(self):
         return self.name