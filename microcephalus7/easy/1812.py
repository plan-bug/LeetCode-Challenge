# 짝 홀
# 나머지에 따라 판별
# 영어도 ascii 코드로 나누기

class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        return ord(coordinates[0]) %2 != int(coordinates[1])%2