import math as mt
import random as rdm
from Sector import Sector

class Stock:
    def __init__(self, name:str, price:float, mu:float, sector:'Sector', sigma:float) -> None:
        self._name = name
        self._price = price
        self._mu = mu
        self._sector = sector
        self._sigma = sigma
        self._history = [price]

    def getName(self) -> str:
        return self._name
    
    def getPrice(self) -> float:
        return self._price
    
    def getSector(self) -> 'Sector':
        return self._sector
        
    def updatePrice(self, event_boost=0.0) -> None:
        dt = 1
        z = rdm.gauss(0, 1)
        sector_influence = self._sector.trend
        new_mu = self._mu + sector_influence + event_boost
        change_factor = mt.exp((new_mu - 0.5 * self._sigma ** 2) * dt + self._sigma * mt.sqrt(dt) * z)
        self._price *= change_factor
        self._price = round(self._price, 2)
        self._history.append(self._price)
    
    def momentumBias(self) -> None:
        lastMoves = [self._history[i+1] - self._history[i] for i in range(-4, -1)]
        upTrend = sum(1 for x in lastMoves if x > 0)
        downTrend = sum(1 for x in lastMoves if x < 0)
        if upTrend >= 3:
            self._mu += 0.01
        else:
            self._mu -= 0.01