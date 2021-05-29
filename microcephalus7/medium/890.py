# ascii 코드 이용
# pattern ascii 코드로 변환
# 이러터레이러 돌며 pattern element 들 pattern[0] 으로 뺌
# words 돌며 동일 절차 후 pattern 과 비교 

class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        
        def helper( s ):
            
            char_index_dict = dict()
            
            for character in s:
                
                if character not in char_index_dict:
                    char_index_dict[character] = str( len(char_index_dict) )
        
            return ''.join( map(char_index_dict.get, s) )   
            
        pattern_string = helper(pattern)
        
        return [ word for word in words if helper(word) == pattern_string ]