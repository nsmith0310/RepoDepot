class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        
        lim = len(s1)
        a = [ord(s1[i]) for i in range(0,lim)]
        b = [ord(s2[i]) for i in range(0,lim)]
        
        a.sort()
        b.sort()
        
        c1 = 0
        c2 = 0
        
        i = 0
        while i<len(a):
            if a[i]>b[i]:c1+=1
            elif b[i]>a[i]:c2+=1
            else:
                c1+=1
                c2+=1
            i+=1
        return (c1>=lim or c2>=lim)
