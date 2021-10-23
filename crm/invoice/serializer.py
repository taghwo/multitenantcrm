from typing import Dict
from customexceptions.ValidateException import ValidationException
from tenant.serializer import TenantNestedSerializer
from account.serializer import AccountNestedSerializer
from rest_framework.exceptions import ValidationError
from rest_framework import serializers, validators
from modules.Util import json_to_dict
from .models import Invoice

class InvoiceReadSerializer(serializers.ModelSerializer):

    created_by = AccountNestedSerializer(read_only=True)
    updated_by = AccountNestedSerializer(read_only=True)
    assigned_to = AccountNestedSerializer(read_only=True)
    tenant = TenantNestedSerializer(read_only=True)

    class Meta:
        model = Invoice
        fields = '__all__'
        depth = 1
        ordering = ['-created_at']

class InvoiceWriteSerializer(serializers.ModelSerializer):
    contact = serializers.IntegerField(required=True)
    due_date = serializers.DateTimeField(required=True)
    number = serializers.IntegerField(required=True,min_value=1)
    items = serializers.JSONField(required=True)
    status = serializers.CharField(required=False, max_length=50)
    is_drafted = serializers.BooleanField(required=False)
    sub_total = serializers.IntegerField(required=False, min_value=1)
    total = serializers.IntegerField(required=True)
    template = serializers.IntegerField(required=True)
    issued_date = serializers.DateField(required=False)

    class Meta:
        model = Invoice
        fields = '__all__'
        read_only_fields  = ['id']

    def validate_status(self,value):
         if value.lower()  not in ['pending','cleared','cancelled']:
             raise ValidationError('available options are pending, cleared, cancelled')

         return value

    def validate_items(self,value):
         expected_keys = ['description', 'quantity','unit_price', 'amount']
         error_bag = []

         if not isinstance(value, list):
                raise ValidationError("Item must be an array of object")

         for item in value:
             if not isinstance(item, dict):
                raise ValidationError("Single item must be an array, like {'description':'testing','quantity':'10', 'unit_price':'100','amount':'1000'}")

             missing_keys = set(expected_keys).difference(item.keys())

             if missing_keys :
                 error_bag.extend(list(missing_keys))
                 break

         if error_bag:
             raise ValidationError(f"Your invoice items list is missing these fields: {error_bag}")

         return value