class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        max_element = 0
        chunks = 0
        for i , val in enumerate(arr):
            max_element = max(max_element,val)
            if max_element == i:
                chunks += 1
        return chunks
