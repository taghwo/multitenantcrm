from customexceptions.ValidateException import ValidationException
from rest_framework.exceptions import ValidationError
from .models import Type
from rest_framework import serializers

class ClientTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = ('id','name','created_at')
        depth = 1
        read_only_fields  = ['id']

    def validate_name(self,value):
         type = Type.objects.filter(name=value).filter(tenant__id=self.context['tenant_id'])
         if len(type) > 0:
            raise serializers.ValidationError('Sorry you already created a type with that name')
         return value
