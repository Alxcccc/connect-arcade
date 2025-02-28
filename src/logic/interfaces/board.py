from abc import abstractmethod, ABC

class Board(ABC):
    
    @abstractmethod
    def create_board(self):
        pass
    
    @abstractmethod
    def get_board(self):
        pass
        
    @abstractmethod
    def show_matrix(self):
        pass
            
    @abstractmethod
    def reset_matrix(self):
        pass
    
    @abstractmethod
    def put_token(self):
        pass