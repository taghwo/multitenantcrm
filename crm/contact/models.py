from account.models import Account
from django.db import models
from django.db.models.deletion import SET_NULL
from type.models import Type
from company.models import Company
from tenant.models import Tenant
from django.utils.timezone import now

class Contact(models.Model):
    SALUTAION_CHIOCES = (
        ('mr','MR'),
        ('mrs','MRS'),
        ('dr','DR'),
        ('Engr','Engr'),
        ('miss','Miss')
    )

    first_name = models.CharField(null=False,blank=False,max_length=1000)
    last_name = models.CharField(null=False,blank=False,max_length=1000)
    salutation = models.CharField(choices=SALUTAION_CHIOCES,null=True,blank=True,max_length=200)
    position = models.CharField(null=True,blank=True,max_length=500)
    address = models.CharField(null=True,blank=True,max_length=1000)
    emails = models.CharField(null=False,blank=False,max_length=1000,help_text="enter comma separated email address")
    phone_numbers = models.CharField(null=True,blank=True,max_length=1000,help_text="enter comma separated phone numbers address")
    address = models.CharField(null=True,blank=True,max_length=250)
    website = models.CharField(null=True,blank=True,max_length=250)
    country = models.CharField(null=True,blank=True,max_length=500)
    region = models.CharField(null=True,blank=True,max_length=500)
    city = models.CharField(null=True,blank=True,max_length=500)
    social_accounts = models.JSONField(null=True,blank=True,max_length=1000)
    type = models.ForeignKey(Type, related_name="contacts",null=True, blank=True, default=None, on_delete=SET_NULL)
    tenant = models.ForeignKey(Tenant, related_name="contacts",null=True, blank=True,default=None, on_delete=SET_NULL)
    company = models.ForeignKey(Company, related_name="contacts",null=True, blank=True,default=None, on_delete=SET_NULL)
    assigned_to = models.ForeignKey(Account, related_name="userassignedcontacts",null=True, default=None, blank=True, on_delete=SET_NULL)
    created_by = models.ForeignKey(Account, related_name="usercreatedcontacts",null=True, default=None, blank=True, on_delete=SET_NULL)
    updated_by = models.ForeignKey(Account, related_name="userupdatedcontacts",null=True, default=None, blank=True, on_delete=SET_NULL)
    custom_fields = models.JSONField(null=True,blank=True)
    status = models.BooleanField(default=1)
    created_at = models.DateTimeField(default=now)
    updated_at = models.DateTimeField(default=now)
