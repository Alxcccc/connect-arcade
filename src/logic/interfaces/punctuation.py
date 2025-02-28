from abc import abstractmethod, ABC

class Punctuation(ABC):
    
    @abstractmethod
    def show(self):
        pass
    
    @abstractmethod
    def increment_points(self):
        pass
    
    @abstractmethod
    def reset_point(self):
        pass