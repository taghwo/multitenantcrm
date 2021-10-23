
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
