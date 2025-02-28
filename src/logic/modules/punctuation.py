from src.logic.interfaces.punctuation import Punctuation

class Connect4Punctuation(Punctuation):
    
    def __init__(self):
        self.points = {"R": 0, "B": 0}
    
    def show(self):
        return {
            "R": f"Red: {self.points['R']}",
            "B": f"Blue: {self.points['B']}"
        }
        
    def increment_points(self, user: str):
        if user in self.points:
            self.points[user] += 1
    
    def reset_point(self):
        self.points["R"], self.points["B"] = 0, 0