class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        result = []
        index = 1
        for num in target:
            if num == index:
                result.append("Push")
                index += 1
            else:
                while num != index:
                    result.append("Push")
                    result.append("Pop")
                    index += 1
                result.append("Push")
                index += 1
        
        return result
            
