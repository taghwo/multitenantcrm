from django.core.mail import send_mail
from django.template.loader import render_to_string
from abc import ABCMeta, abstractmethod


class BaseMailer(metaclass=ABCMeta):
    __to, __sender,  __html, __text, __subject = '', '', '', '', ''

    @abstractmethod
    def render(self):
        pass

    def subject(self, data: str):
        """
        :param data: str
        :return: object
        """

        if not isinstance(data, str):

            raise ValueError('The subject method only accepts a string. '
                             '"Welcome to example.com"')

        self.__subject = data.capitalize()

        return self

    def template(self, data: list):
        """
        :param data: list
        :return: object
        """

        if not isinstance(data, list):

            raise ValueError('html and txt templates should be entered as a list,'
                             ' ["example.html","example.text".'
                             ' Pay attention to their paths')

        template_data = {}

        for attr, value in vars(self).items():

            if not attr.startswith('_'):

                template_data[attr] = value

        self.__html = render_to_string(data[0], template_data)

        self.__text = render_to_string(data[1], template_data)

        return self

    def to(self, data: str):
        """
        :param data: list | str
        :return: object
        """
        if isinstance(data, list):

            self.__to = data

        else:

            self.__to = []

            self.__to.append(data)

        return self

    def sender(self, data: str):
        """
        :param data: str
        :return: object
        """

        if not isinstance(data, str):

            raise ValueError('The sender method only accepts a string. example "johndoe@gmail.com"')

        self.__sender = data.lower()

        return self

    def send(self):
        try:
            send_mail(self.__subject, self.__text, self.__sender, self.__to,
                      fail_silently=False, html_message=self.__html)

        except Exception as e:

            return e
