import filetype
from customexceptions.ValidateException import ValidationException


class ValidateUploadedFile:
    accepted_file_types = []
    attr = 'file_uploaded'
    max_upload_size = 1999
    file = ''
    file_type = ''

    def __init__(self, **kwargs):

        self.file = kwargs['file']

        if kwargs.get('attr'):
            self.attr = kwargs['attr']

        self.file_type = filetype.guess(self.file)

        if kwargs.get('max_upload_size'):
            self.max_upload_size = kwargs['max_upload_size']
            self.validate_file_size()

        if kwargs.get('accepted_file_types'):
            if not isinstance(kwargs['accepted_file_types'], list):
                self.accepted_file_types.extend(kwargs['accepted_file_types'])
            else:
                self.accepted_file_types = kwargs['accepted_file_types']

            self.validate_file_type()

    def validate_file_type(self):
        if self.file_type.extension not in self.accepted_file_types:
            message = [f'only {self.accepted_file_types} can be uploaded']
            raise ValidationException(upload_error=self.format_error_msg(message))

    def validate_file_size(self):

        if self.file.size/1000 > self.max_upload_size:
            message = [f'uploaded file cannot be greater than {self.max_upload_size/1000} mb']
            raise ValidationException(errors=self.format_error_msg(message))

    def format_error_msg(self, message):
        return {self.attr: message}

    def get_file_extension(self):
        return self.file_type.extension
