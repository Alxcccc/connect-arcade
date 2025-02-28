from abc import abstractmethod, ABC

class Menu(ABC):
    
    @abstractmethod
    def show_menu(self):
        pass
    
    @abstractmethod
    def show_options(self):
        pass
    
    @abstractmethod
    def catch_option(self):
        pass
    
    @abstractmethod
    def call_fuctions(self):
        pass
    
