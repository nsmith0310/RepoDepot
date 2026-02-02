class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        
        def ship(cap,lim):
            d = 1
            
            count = weights[0]
            k = 0
            i = 0
            for i in range(1,lim):
                if count+weights[i]>cap:
                    d+=1
                    count = weights[i]
                else:
                    count+=weights[i]
                
                
            return d
        
        
        
        lim = len(weights)
        
        mx = max(weights)
        l = mx
        h = sum(weights)
        
        l_val = 0
        h_val = 0
        while l<=h:
            m = (l+h)//2
            f = ship(m,lim)
            if f<=D:
                h = m-1
                
                m = (l+h)//2
            else:
                l = m+1
               
                m = (l+h)//2
                
        l1 = ship(l,lim)
        h1 = ship(h,lim)
        if l1>D or l<mx:
            return h
        if h1>D or h<mx:
            return l
        else:
            return min(l,h)
        
