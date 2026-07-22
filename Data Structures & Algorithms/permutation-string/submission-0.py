

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1=sorted(s1)
        for i in range(len(s2)):
            for j in range(i,len(s2)):
                substr1=s2[i : j + 1]
                substr=sorted(substr1)
                if substr == s1:
                    return True
        return False