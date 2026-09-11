import re

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # Find all words using regex
        words = re.findall(r'\S+', s)
        
        # Return length of the last word
        return len(words[-1])