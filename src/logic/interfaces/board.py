from abc import abstractmethod, ABC
from typing import Optional, Tuple, List

from src.logic.enums import Token


class BoardModel(ABC):
    @property
    @abstractmethod
    def row_count(self) -> int:
        ...

    @property
    @abstractmethod
    def col_count(self) -> int:
        ...

    @property
    @abstractmethod
    def turn(self) -> Token:
        ...

    @turn.setter
    @abstractmethod
    def turn(self, value: Token) -> None:
        ...

    @abstractmethod
    def create_board(self) -> None:
        ...

    @abstractmethod
    def get_board(self) -> List[List[str]]:
        ...

    @abstractmethod
    def clear_board(self) -> None:
        ...

    @abstractmethod
    def put_token(self, col: int) -> Optional[Tuple[int, int]]:
        ...
