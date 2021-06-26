from collections import defaultdict
from typing import DefaultDict


class UndergroundSystem:
    def __init__(self):
        self.passenger = DefaultDict(tuple)
        self.trafficRecord = defaultdict(list)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.passenger[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStation, startTime = self.passenger[id]
        endStation, endTime = stationName, t

        self.trafficRecord[(startStation, endStation)].append(endTime - startTime)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        traffic = self.trafficRecord[(startStation, endStation)]

        return sum(traffic) / len(traffic)
