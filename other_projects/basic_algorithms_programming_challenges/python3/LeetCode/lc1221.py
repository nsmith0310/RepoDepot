class Solution:
    def balancedStringSplit(self, s: str) -> int:
        if len(s)<2:
            return 0
        t = len(s)
        f = []
        i = 1
        while i<=len(s):
            tmp = s[:i]
            if tmp.count('R')==tmp.count('L'):
                f.append(tmp)
                s=s[i:]
                i=0
        
            i+=1
            
        return len(f)
