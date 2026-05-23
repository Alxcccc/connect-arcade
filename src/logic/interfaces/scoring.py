from abc import abstractmethod, ABC
from typing import Dict


class ScoreTracker(ABC):
    @abstractmethod
    def show(self) -> Dict[str, str]:
        pass

    @abstractmethod
    def increment_points(self, player: str) -> None:
        pass

    @abstractmethod
    def reset_points(self) -> None:
        pass
