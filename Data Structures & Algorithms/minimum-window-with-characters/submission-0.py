from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t:
            return ""
        
        countT = Counter(t)
        window = {}
        
        have, need = 0, len(countT)
        res = [-1, -1]
        resLen = float("inf")
        left = 0
        
        for right in range(len(s)):
            char = s[right]
            window[char] = window.get(char, 0) + 1
            
            if char in countT and window[char] == countT[char]:
                have += 1
            
            while have == need:
                # Update result
                if (right - left + 1) < resLen:
                    res = [left, right]
                    resLen = right - left + 1
                
                # Pop from left
                window[s[left]] -= 1
                if s[left] in countT and window[s[left]] < countT[s[left]]:
                    have -= 1
                left += 1
        
        l, r = res
        return s[l:r+1] if resLen != float("inf") else ""