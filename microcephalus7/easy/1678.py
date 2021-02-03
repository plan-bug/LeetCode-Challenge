# ( ) 기준으로 split
# i 마다 if 문으로 판별
class Solution:
    def interpret(self, command: str) -> str:
        
        word = ''
        result = ''
        for i in command:
            word += i
            if word == 'G' :
                result+='G'
                word=''
            if word == '()':
                result+='o'
                word =''
            if word == '(al)':
                result+='al'
                word = ''
        return result

