from abc import ABC, abstractmethod

class Challenge(ABC):
    def __init__(self, file):
        with open(file, 'r') as f:
            self.content = f.readlines()
    
    @abstractmethod
    def execute(self):
        return NotImplemented
