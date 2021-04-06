from rest_framework import serializers
from account.models import Account
from django.utils.text import gettext_lazy as _
from rest_framework_simplejwt.tokens import RefreshToken, TokenError
from tenant.serializer import TenantSerializer


class AuthenticationSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True, allow_blank=False, allow_null=False, min_length=2)
    password = serializers.CharField(required=True, allow_blank=False, allow_null=False, min_length=6)

    class Meta:
        fields = ('email', 'password')


class RegistrationSerializer(serializers.ModelSerializer):
    tenant = TenantSerializer(read_only=True)

    def validate_password(self, value):
        if value and self.context['request'].data['password_confirmation'] \
                and self.context['request'].data['password_confirmation'] != value:
            raise serializers.ValidationError('Passwords submitted do not match')
        return value

    def create(self, validated_data):
        user = Account.objects.create_tenant_user(email=validated_data['email'],username=validated_data['username'],
                    password=validated_data['password'],fullname=validated_data['fullname'])
        user.save()
        return user

    class Meta:
        model = Account
        extra_kwargs = {'password': {'write_only': True}}
        fields = '__all__'
        # depth = 1


class UserSerializer(serializers.ModelSerializer):
    tenant = TenantSerializer()

    class Meta:
        model = Account
        exclude = ("password",)


class RefreshTokenSerializer(serializers.Serializer):
    refresh = serializers.CharField()

    default_error_messages = {
        'bad_token': _('Token is invalid or expired')
    }

    def validate(self, attrs):
        self.token = attrs['refresh']
        return attrs

    def save(self, **kwargs):
        try:
            RefreshToken(self.token).blacklist()
        except TokenError:
            self.fail('bad_token')