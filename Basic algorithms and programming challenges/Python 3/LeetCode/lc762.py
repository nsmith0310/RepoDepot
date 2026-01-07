class Solution:
    def countPrimeSetBits(self, L: int, R: int) -> int:
        l = [str(bin(x))[2:] for x in range(L,R+1)]
        l2 = []
        i = 0
        while i<len(l):
            t = (l[i].count('1'))
            if t>1:
                l2.append(t)
            i+=1
        if l2==[]:
            
            return 0
        
        c = 0
        for x in l2:
            if x==2:
                c+=1
            else:
                t=0
                i = 2
                while i<x:
                    if x%i==0:
                        t=1
                        break
                    i+=1
                if t==0:
                    c+=1
        return c
                        
        
