# 포인트 잘 움직이기

class OrderedStream:

    def __init__(self, n: int):
        
        self.a = [None] * (n+2)
        self.i = 1
        
        

    def insert(self, idKey: int, value: str) -> List[str]:
        a = self.a
        i = self.i 
        a[idKey] = value
        if a[i]:
            self.i = a.index(None, i+1)
            return a[i:self.i]
        