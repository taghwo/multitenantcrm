from django.db.models.deletion import SET_NULL
from django.utils.timezone import now
from django.db import models
from tenant.models import Tenant
from account.models import Account
class Task(models.Model):
     title = models.CharField(null=False,blank=False,max_length=500)
     detail = models.TextField(null=True,blank=True,max_length=3000)
     status = models.CharField(choices=[('pending','pending'),('in progress','in progress'),('completed','completed')],blank=True,null=True, default="pending",max_length=500)
     due_date = models.DateTimeField(null=False, blank=False, default=None)
     created_at = models.DateTimeField(default=now)
     updated_at = models.DateTimeField(default=now)
     tenant = models.ForeignKey(Tenant, related_name='tasks',null=True, default=None, on_delete=SET_NULL)
     created_by = models.ForeignKey(Account, related_name="createdtasks",null=True, default=None, blank=True, on_delete=SET_NULL)
     assigned_to = models.ForeignKey(Account, related_name="assignedtasks",null=True, default=None, blank=True, on_delete=SET_NULL)
     updated_by = models.ForeignKey(Account, related_name="updatedtasks",null=True, default=None, blank=True, on_delete=SET_NULL)
     custom_status = models.JSONField(null=True,blank=True)

     class meta:
         ordering = ['created_at']
         verbose_name_plural = ['tasks']

     def __str__(self):
         return self.title