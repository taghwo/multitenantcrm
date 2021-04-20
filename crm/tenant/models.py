from django.db import models
from django.utils.timezone import now
# from account.models import Account


# Create your models here.
class Tenant(models.Model):
    # industry_choices = (
    #     ('tech','technology')
    #     ('edu','education')
    #     ('ICT','Technology')
    #     ('Agro','Agriculture')
    #     ('Inf0','Information')
    #     ('NGO','NGO')
    # )
    name = models.CharField(unique=True, max_length=100, null=False, blank=False, help_text="Enter business name")
    business_email = models.EmailField(
        null=False,
        blank=False,
        max_length=255,
        unique=False,
        default="example@email.com"
    )
    address = models.CharField(unique=False, max_length=1000, null=True, blank=True, help_text="Enter business address")
    number_of_staffs = models.PositiveBigIntegerField(unique=False, null=True, default=0, blank=True, help_text="Enter name address")
    industry = models.CharField(unique=False, max_length=1000, null=True, blank=True, help_text="Select a niche for your company")
    modules = models.CharField(unique=False, max_length=1000, null=True, blank=True, default="CRM", help_text="Select modules you want to use")
    banner = models.FileField(upload_to='banner/', null=True, blank=True)
    logo = models.FileField(upload_to='logo/', null=True, blank=True)
    created_at = models.DateTimeField(default=now)
    updated_at = models.DateTimeField(default=now)

    class Meta:
        verbose_name_plural = 'Tenants'
        db_table = 'tenants'
        ordering = ['name']

    def __str__(self):
        return self.name