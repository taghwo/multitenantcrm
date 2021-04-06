from django.db.models import fields
from rest_framework import serializers
from account.models import Account


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        extra_kwargs = {'password': {'write_only': True}}
        fields = '__all__'


class AccountNestedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['email','fullname','username','is_active']

