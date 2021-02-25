class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        total_line = 1
        pixels = 0
        to_zero = 97
        for c in s:
            next_value = widths[ord(c) - to_zero]
            if (pixels + next_value) > 100:
                pixels = next_value
                total_line += 1
            else:
                pixels += next_value
                
        return [total_line, pixels]
