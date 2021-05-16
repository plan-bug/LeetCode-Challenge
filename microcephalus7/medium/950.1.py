class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort(reverse=True)
        result = [deck.pop(0)]
        for i in deck:
            result.append(result.pop(0))
            result.append(i)
        return result[::-1]