class Solution:
    def maxScore(self, s: str) -> int:
        
        
        mx = 0
        
        i = 0
        while i<len(s)-1:
            count = s[:i+1].count('0')+s[i+1:].count("1")
            if count>mx:
                mx = count
            i+=1
        return mx
        
        
        
