# ( ) 기준으로 split
# i 마다 if 문으로 판별
class Solution:
    def interpret(self, command: str) -> str:
        return ['G' for i in command.split('(')]