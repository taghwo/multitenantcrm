from customexceptions.ValidateException import ValidationException
from tenant.serializer import TenantNestedSerializer
from account.serializer import AccountNestedSerializer
from rest_framework.exceptions import ValidationError
from .models import Task
from account.models import Account
from rest_framework import serializers


class TaskReadSerializer(serializers.ModelSerializer):

    created_by = AccountNestedSerializer(read_only=True)
    updated_by = AccountNestedSerializer(read_only=True)
    assigned_to = AccountNestedSerializer(read_only=True)
    tenant = TenantNestedSerializer(read_only=True)

    class Meta:
        model = Task
        fields = '__all__'
        depth = 1

class TaskWriteSerializer(serializers.ModelSerializer):

    assigned_to = serializers.IntegerField(required=False,write_only=True)
    custom_status = serializers.JSONField(required=False)
    due_date = serializers.DateField(required=True, input_formats=['%d-%m-%Y', '%Y-%m-%d'])

    class Meta:
        model = Task
        fields = '__all__'
        read_only_fields  = ['id']


    def validate_custom_status(self,value):
         if value and  not isinstance(value,list):
             raise ValidationError('custom status must be an array of strings')
         return value

    def validate_assigned_to(self,value):
         user = Account.objects.filter(tenant__id=self.context['tenant_id'],id=value).first()
         if user is not None:
             return user
         raise  ValidationError("User to assign task to was not found")

    def validate_status(self,value):
         if value.lower()  not in ['pending','in progress','completed']:
             raise ValidationError('available options are pending,in progress,completed')
         return value