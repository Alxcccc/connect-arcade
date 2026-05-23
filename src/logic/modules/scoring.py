from typing import Dict

from src.logic.interfaces.scoring import ScoreTracker


class Connect4ScoreTracker(ScoreTracker):
    def __init__(self) -> None:
        self.scores: Dict[str, int] = {"R": 0, "B": 0}

    def show(self) -> Dict[str, str]:
        return {
            "R": f"Red: {self.scores['R']}",
            "B": f"Yellow: {self.scores['B']}"
        }

    def increment_points(self, player: str) -> None:
        if player in self.scores:
            self.scores[player] += 1

    def reset_points(self) -> None:
        self.scores["R"], self.scores["B"] = 0, 0
