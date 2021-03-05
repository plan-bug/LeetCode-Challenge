class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = []
        for i, num in enumerate(prices):
            while (stack and prices[stack[-1]] >=num):
                popIndex = stack.pop()
                prices[popIndex]-=num
            stack.append(i)
        return prices