from tenant.serializer import TenantNestedSerializer
from account.serializer import AccountNestedSerializer
from rest_framework.exceptions import ValidationError
from .models import Transaction
from rest_framework import serializers


class TransactionReadSerializer(serializers.ModelSerializer):
    created_by = AccountNestedSerializer(read_only=True)
    updated_by = AccountNestedSerializer(read_only=True)
    tenant = TenantNestedSerializer(read_only=True)
    fee_to_string = serializers.SerializerMethodField()

    class Meta:
        model = Transaction
        fields = '__all__'
        depth = 1

    def get_fee_to_string(self,obj):
            return obj.fee_to_string

class TransactionWriteSerializer(serializers.ModelSerializer):
    custom_fields = serializers.JSONField(required=False)
    type = serializers.CharField(required=False)
    status = serializers.CharField(required=False)

    class Meta:
        model = Transaction
        fields = '__all__'
        read_only_fields  = ['uuid']

    def validate_custom_fields(self,value):
         if value and  not isinstance(value,list):
             raise ValidationError('custom fields must be an array of strings')
         return value

    def validate_type(self,value):
         if value and value.lower()  not in ['onetime','re-occuring']:
             raise ValidationError('available options are onetime and re-occuring')
         return value

    def validate_status(self,value):
         if value and value.lower()  not in ['pending','cleared']:
             raise ValidationError('available options are pending and cleared')
         return value