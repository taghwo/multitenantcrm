from django.db.models import fields
from rest_framework import serializers
from .models import Feedback
class FeedbackSerializer(serializers.ModelSerializer):

    class Meta:
        model = Feedback
        fields = '__all__'

    def validate(self, attrs):
        if not 'email' in attrs and not 'phonenumber' in attrs:
            raise serializers.ValidationError({"email":["You need to provide either email or phonenumber"]})

        if not attrs['email'] and not attrs['phonenumber']:
            raise serializers.ValidationError({"email":["You need to provide either email or phonenumber"]})

        return attrs