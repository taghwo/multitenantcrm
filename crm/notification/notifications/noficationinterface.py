from abc import ABCMeta, abstractmethod

class NoficationInterface(metaclass=ABCMeta):
    @abstractmethod
    def via(self):
        pass

    def notify(self):
        channels = self.via()
        for channel in channels:
            getattr(self, 'to_'+channel)()