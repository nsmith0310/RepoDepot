class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        s = list(S)
        t = list(T)
        
        while s[0]=="#":
            del S[0]
        while t[0]=="#":
            del t[0]
            
            
        i = 0
        while i<len(s):
            if s[i]=="#":
                del s[i]
                if i>0:
                    del s[i-1]
                i=0
            else:
                i+=1
        i = 0
        while i<len(t):
            if t[i]=="#":
                del t[i]
                if i>0:
                    del t[i-1]
                i=0
            else:
                i+=1
        return s==t
