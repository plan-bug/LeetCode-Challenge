

import itertools

from collections import deque

class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):    
        self.combinations = deque(list(itertools.combinations(characters,combinationLength)))
        
        
    def next(self) -> str:
        return ''.join(self.combinations.popleft())
        
    def hasNext(self) -> bool:
        return True if self.combinations else False