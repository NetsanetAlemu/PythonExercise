from abc import ABC, abstractmethod

class Arithmetic(ABC):
    
    @abstractmethod
    def add(self):
        pass

    @abstractmethod
    def subtract(self):
        pass

    @abstractmethod
    def multiply(self):
        pass

    @abstractmethod
    def divide(self):
        pass

