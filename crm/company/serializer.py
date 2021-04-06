
from django.core.exceptions import ValidationError
from tenant.serializer import TenantNestedSerializer
from account.serializer import AccountNestedSerializer
from .models import Company
from rest_framework import serializers


class CompanyNestedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('id','name')

class CompanySerializer(serializers.ModelSerializer):
    created_by = AccountNestedSerializer(read_only=True)
    updated_by = AccountNestedSerializer(read_only=True)
    tenant = TenantNestedSerializer(read_only=True)
    industry = serializers.CharField(required=True)

    emails = serializers.JSONField(required=True,error_messages={
            "required": "enter list of comma separated email adresses",
        })
    social_accounts = serializers.JSONField(required=False)
    phone_numbers = serializers.JSONField(required=True)

    class Meta:
        model = Company
        fields = '__all__'
        depth = 1
        read_only_fields  = ['id']

    def validate_name(self,value):
         company = Company.objects.filter(name=value.lower()).filter(tenant__id=self.context['tenant_id']).first()

         if company and company.id != self.context['pk']:
            raise serializers.ValidationError('Sorry you already created a company with that name')
         return value

    def validate_emails(self,value):
         if value and  not isinstance(value,list):
             raise ValidationError('email must be an array of emails addresses')
         return value

    def validate_phone_numbers(self,value):
         if value and not isinstance(value,list):
             raise ValidationError('phone numbera must be an array with string of phone numbers')
         return value

    def validate_social_accounts(self,value):
         if value and not isinstance(value,list):
             raise ValidationError('must be an array of objects with value key pairs')
         return value

    def validate_industry(self,value):
         if value.lower()  not in ['technology','education','ngo']:
             raise ValidationError('available options are technology,education,ngo')
         return value
    def validate_custom_fields(self,value):
          if value and not isinstance(value,list):
             raise ValidationError('must be an array of objects with value key pairs')
          return value


    # name = models.CharField(null=False,blank=False,max_length=1000)
    # description = models.CharField(null=True,blank=True,max_length=1000)
    # name_of_ceo = models.CharField(null=True,blank=True,max_length=500)
    # address = models.CharField(null=True,blank=True,max_length=1000)
    # emails = models.CharField(null=True,blank=True,max_length=1000,help_text="enter comma separated email address")
    # phone_numbers = models.CharField(null=True,blank=True,max_length=1000,help_text="enter comma separated phone numbers address")
    # website = models.CharField(null=True,blank=True,max_length=250)
    # country = models.CharField(null=True,blank=True,max_length=500)
    # region = models.CharField(null=True,blank=True,max_length=500)
    # city = models.CharField(null=True,blank=True,max_length=500)
    # industry = models.CharField(null=True,blank=True,max_length=500)
    # social_accounts = models.JSONField(null=True,blank=True,max_length=1000)
    # tenant = models.ForeignKey(Tenant, related_name="companies",null=True, blank=True,default='unknown', on_delete=SET_NULL)
    # created_by = models.ForeignKey(Account, related_name="usercreatedcompany",null=True, default='unknown', blank=True, on_delete=SET_NULL)
    # updated_by = models.ForeignKey(Account, related_name="userupdatedbycompany",null=True, default='unknown', blank=True, on_delete=SET_NULL)
    # custom_fields = models.JSONField(null=True,blank=True)
    # status = models.BooleanField(default=1)