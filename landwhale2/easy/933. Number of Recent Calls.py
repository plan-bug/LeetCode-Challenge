class RecentCounter:

    def __init__(self):
        self.pingTimes = []

    def ping(self, t: int) -> int:
        self.pingTimes.append(t)
        while self.pingTimes[0] < t - 3000:
            self.pingTimes.pop(0)
        
        return len(self.pingTimes)
            


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
