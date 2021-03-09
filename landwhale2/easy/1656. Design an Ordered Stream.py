class OrderedStream:

    def __init__(self, n: int):
        self.stream = [None]*(n+1)
        self.lowestId = 1

    def insert(self, idKey: int, value: str) -> List[str]:
        nextEl = []
        self.stream[idKey] = value
        if idKey > self.lowestId:
            return []
        else:
            for i in range(self.lowestId,len(self.stream)):
                if self.stream[i] is None:
                    self.lowestId = i
                    break
                else:
                    nextEl.append(self.stream[i])
        return nextEl    


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)
