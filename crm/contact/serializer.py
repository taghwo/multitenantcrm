from type.serializer import ClientTypeSerializer
from company.serializer import CompanyNestedSerializer, CompanySerializer
from type.models import Type
from company.models import Company
from rest_framework.exceptions import ValidationError
from .models import Contact
from tenant.serializer import TenantNestedSerializer
from account.serializer import AccountNestedSerializer
from rest_framework import serializers

class ContactReadOnlySerializer(serializers.ModelSerializer):
    created_by = AccountNestedSerializer(read_only=True)
    updated_by = AccountNestedSerializer (read_only=True)
    tenant = TenantNestedSerializer(read_only=True)
    company = CompanyNestedSerializer(read_only=True)
    type = ClientTypeSerializer(read_only=True)

    class Meta:
        model = Contact
        fields = '__all__'
        depth = 1
        read_only_fields  = ['id']


class ContactWriteSerializer(serializers.ModelSerializer):
    created_by = AccountNestedSerializer(read_only=True)
    updated_by = AccountNestedSerializer (read_only=True)
    tenant = TenantNestedSerializer(read_only=True)
    company = serializers.IntegerField(required=False,write_only=True)
    type = serializers.IntegerField(required=False,write_only=True)

    emails = serializers.JSONField(required=True,error_messages={
            "required": "enter list of comma separated email adresses",
        })
    social_accounts = serializers.JSONField(required=False)
    phone_numbers = serializers.JSONField(required=True)

    class Meta:
        model = Contact
        fields= '__all__'

    def validate_company(self,value):
         company = Company.objects.filter(pk=value,tenant__id=self.context['tenant_id']).first()
         if company is None:
            raise serializers.ValidationError('The company selected was not found in your created companies list')
         return company

    def validate_type(self,value):
         type = Type.objects.filter(pk=value, tenant__id=self.context['tenant_id']).first()
         if type is None:
            raise serializers.ValidationError('The type selected was not found in your created types')
         return type

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
