from rest_framework import serializers
from invoicetemplate.models import InvoiceTemplate
from tenant.serializer import TenantNestedSerializer
from modules.FileTypeValidator import ValidateUploadedFile
from modules.Util import rand_uuid_str
class InvoiceTemplateSerializer(serializers.ModelSerializer):
    tenant = TenantNestedSerializer(read_only=True)

    class Meta:
        model = InvoiceTemplate
        fields = '__all__'
        depth = 2


    def validate_cover(self, value):
        accepted_files = 'png', 'jpg', 'gif', 'jpeg'

        file = ValidateUploadedFile(file=value, accepted_file_types=accepted_files, attr='cover')

        filename = self.get_initial()['name'].replace(' ', '-')

        value.name = f"{filename.lower()[:6]}-{rand_uuid_str()}.{file.get_file_extension()}"

        return value

