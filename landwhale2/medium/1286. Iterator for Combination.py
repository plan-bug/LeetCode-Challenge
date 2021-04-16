class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.characters=characters
        self.count=0
        self.list_characters=list(characters)
        self.combinations=list(combinations(self.list_characters,combinationLength))
        

    def next(self) -> str:
        x=list(self.combinations[self.count])
        self.count += 1
        return ''.join(x)
        
        
        
        

    def hasNext(self) -> bool:
        if self.count < len(self.combinations):
            return True
