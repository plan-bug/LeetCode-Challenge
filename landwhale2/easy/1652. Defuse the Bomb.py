# 빨리 짜긴 했는데 진짜 생각없이 짠 코드

class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        if k == 0:
            return [0 for i in range(len(code))]
        
        result = []
        for i in range(len(code)):
            
            if k > 0:
                count = k
            else:
                count = -k
            total = 0
            p = 1
            if k > 0:
                while count:
                    count -= 1
                    total += code[(i+p) % len(code)]
                    p += 1
            else:
                while count:
                    count -= 1
                    total += code[(i-p) % len(code)]
                    p += 1
            
            result.append(total)
            
        return result
