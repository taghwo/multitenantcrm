from rest_framework import serializers
from tenant.models import Tenant
from account.models import Account
from modules.FileTypeValidator import ValidateUploadedFile
from account.serializer import AccountNestedSerializer, AccountSerializer
from modules.Util import rand_uuid_str

class TenantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tenant
        fields = ('id','name','address', 'banner','number_of_staffs','industry','business_email','modules','logo','created_at')
        depth = 2

    def validate_banner(self, value):
        accepted_files = 'png', 'jpg', 'gif', 'jpeg'

        file = ValidateUploadedFile(file=value, accepted_file_types=accepted_files, attr='banner')

        filename = self.get_initial()['name'].replace(' ', '-')

        value.name = f"{filename.lower()[:6]}-{rand_uuid_str()}.{file.get_file_extension()}"

        return value

    def validate_logo(self, value):
        accepted_files = 'png', 'jpg', 'gif', 'jpeg'

        file = ValidateUploadedFile(file=value, accepted_file_types=accepted_files, attr='logo')

        filename = self.get_initial()['name'].replace(' ', '-')

        value.name = f"{filename.lower()[:6]}-{rand_uuid_str()}.{file.get_file_extension()}"

        return value


class TenantAccountsSerializer(serializers.ModelSerializer):
    accounts = AccountNestedSerializer(read_only=True, many=True)

    class Meta:
        model = Tenant
        fields = ('id','name','address', 'banner','number_of_staffs','industry','modules','logo','created_at','accounts')
        depth = 1

class TenantNestedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tenant
        fields = ('id','name')



