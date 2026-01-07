class Solution:
    def maxPower(self, s: str) -> int:
        
        
        mx = 1
        c=1
        i = 1
        while i<len(s):
            if ord(s[i])==ord(s[i-1]):
                c+=1
                if c>mx:
                    mx = c
            else:
                c = 1
            i+=1
        return mx
