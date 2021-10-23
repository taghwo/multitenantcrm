from abc import ABCMeta, abstractmethod

class BaseSMS(metaclass=ABCMeta):
    __phone_number, __body,  __dnd_mode, __subject = '', '', '', ''

    @abstractmethod
    def send(self):
        pass

