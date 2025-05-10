from random import uniform
class Sector:
    def __init__(self, name:str) -> None:
        self.name = name
        self.trend = 0

    def updateTrend(self):
        self.trend = uniform(-0.5, 0.5)
        