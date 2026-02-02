class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        def eat(speed):
            
            h = 0
            for x in piles:
                if speed>=x:
                    h+=1
                else:
                    h+=x//speed + 1
                    
            return h
        
        
        
        l = 1
        h = max(piles)
        while l<=h:
            
            m = (l+h)//2
            if m==0:
                break
            hours = eat(m)
            if hours<=H:
                h = m-1
            else:
                l = m+1
        if l==0:return h
        if h==0:return l
        v1 = eat(l)
        v2 = eat(h)
        if v1>H:
            return h
        elif v2>H:
            return l
        else:
            return min(l,h)
                    
