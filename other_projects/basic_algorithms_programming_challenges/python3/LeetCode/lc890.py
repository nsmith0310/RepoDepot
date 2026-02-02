class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        
        p = pattern
        
        
        l = []
        s=""
        i = 0
        while i<len(p):
            if p[i] not in l:
                l.append(p[i])
                s+=str(i)
            else:
                s+=str(l.index(p[i]))
            i+=1
        f = []
        for x in words:
            q = x
        
        
            l2 = []
            s2=""
            i = 0
            while i<len(q):
                if q[i] not in l2:
                    l2.append(q[i])
                    s2+=str(i)
                else:
                    s2+=str(l2.index(q[i]))
                i+=1
            if s2==s:
                f.append(x)
        return f
