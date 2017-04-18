from abc import abstractmethod


class Processor:
    
    @abstractmethod
    def init(self):
        pass
    
    @abstractmethod
    def process(self):
        pass