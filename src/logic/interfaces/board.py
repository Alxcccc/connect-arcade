from abc import abstractmethod, ABC
from typing import Optional, Tuple, List


class Board(ABC):
    @abstractmethod
    def create_board(self) -> None:
        pass

    @abstractmethod
    def get_board(self) -> List[List[str]]:
        pass

    @abstractmethod
    def draw_board(self) -> None:
        pass

    @abstractmethod
    def clear_board(self) -> None:
        pass

    @abstractmethod
    def put_token(self, x: int, y: int) -> Optional[Tuple[int, int]]:
        pass
