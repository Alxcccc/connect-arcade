from logic.interfaces.strategy import Strategy

class Context():
    def __init__(self, strategy: Strategy) -> None:
        self._strategy = strategy
        
    @property
    def strategy(self) -> Strategy:
        return self._strategy
    
    @strategy.setter
    def strategy(self, strategy: Strategy) -> None:
        self._strategy = strategy
        
    def execute_logic(self) -> None:
        self._strategy.do_algorithm()