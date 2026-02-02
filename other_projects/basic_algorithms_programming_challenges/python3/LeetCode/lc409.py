class Solution:
    def longestPalindrome(self, s: str) -> int:
        s2 = list(set(s))
        c = [s.count(x) for x in s2]
        c2=[]
        p = 0
        for x in c:
            if x&1==True:
                p=1
                c2.append(x-1)
            else:
                c2.append(x)
        
        
        
        t = 0
        for x in c2:
            t+=x
        if p==1:
            return t+1
        else:
            return t
        
