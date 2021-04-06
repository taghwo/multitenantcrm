from account.models import Account
from django.db import models
from django.db.models.deletion import SET_NULL
from tenant.models import Tenant
from django.utils.timezone import now

# Create your models here.
class Company(models.Model):
    name = models.CharField(null=False,blank=False,max_length=1000)
    description = models.TextField(null=True,blank=True)
    name_of_ceo = models.CharField(null=True,blank=True,max_length=500)
    address = models.TextField(null=True,blank=True,max_length=1000)
    emails = models.JSONField(null=False,blank=False,help_text="enter comma separated email address")
    phone_numbers = models.JSONField(null=False,blank=False,default=list)
    website = models.URLField(null=True,blank=True,max_length=500)
    country = models.CharField(null=False,blank=False,max_length=500,default="Unknown")
    region = models.CharField(null=True,blank=True,max_length=500)
    city = models.CharField(null=True,blank=True,max_length=500)
    industry = models.CharField(choices=[('technology','technology'),('education','education'),('ngo','ngo')],blank=False,null=False,max_length=500)
    social_accounts = models.JSONField(null=True,blank=True,max_length=1000)
    tenant = models.ForeignKey(Tenant, related_name="companies",null=True, blank=True,default=None, on_delete=SET_NULL)
    created_by = models.ForeignKey(Account, related_name="usercreatedcompany",null=True, default=None, blank=True, on_delete=SET_NULL)
    updated_by = models.ForeignKey(Account, related_name="userupdatedbycompany",null=True, default=None, blank=True, on_delete=SET_NULL)
    custom_fields = models.JSONField(null=True,blank=True)
    status = models.BooleanField(default=1)
    created_at = models.DateTimeField(default=now)
    updated_at = models.DateTimeField(default=now)


    class meta:
        verbose_plural_name ='companies'
        ordering = ['name']

    def __str__(self):
        return self.name