# 카운터 변수로 대처함

import itertools

class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):    
        self.combinations = list(itertools.combinations(characters,combinationLength))
        self.count= 0
        
    def next(self) -> str:
        self.count +=1
        return ''.join(self.combinations[self.count-1])
        
    def hasNext(self) -> bool:
        return self.count<len(self.combinations)
        


