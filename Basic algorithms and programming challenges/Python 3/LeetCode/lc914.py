from math import sqrt
class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        if len(deck)==1:
            return False
        
        l = list(set(deck))
        l2 = [deck.count(x) for x in l]
        
        m = min(l2)
        f = set()
        while m%2==0:
            f.add(2)
            m//=2
        for i in range(3,int(sqrt(m))+1,2):
            while m%i==0:
                f.add(i)
                m//=i
        
        if m>2:
            f.add(m)
        
        f2 = list(f)
        
        c = 0
        for x in f:
            for y in l2:
                if y%x==0:
                    c+=1
            if c==len(l2):
                return True
            c=0
        return False
    
