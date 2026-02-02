class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        i = 1
        while i<len(s):
            tmp=s[:i]
            tmp2=""
            while len(tmp2)<len(s):
                tmp2+=tmp
            ###print(tmp2)
            if tmp2 == s:
                return True
            i+=1
        return False
