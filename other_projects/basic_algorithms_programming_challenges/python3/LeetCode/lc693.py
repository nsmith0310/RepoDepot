class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        s = str(bin(n))[2:]
        i = 0
        while i<len(s)-1:
            if s[i]==s[i+1]:return False
            i+=1
        return True
