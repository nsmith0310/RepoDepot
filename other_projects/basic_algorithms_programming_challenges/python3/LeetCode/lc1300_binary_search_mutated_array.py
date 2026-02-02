class Solution:
    
    def findBestValue(self, arr: List[int], target: int) -> int:
        def s(val):
            t = 0
            for x in arr:
                if x<=val:
                    t+=x
                else:
                    t+=val
            return t
        
        l = 1
        h = max(arr)
        m = (l+h)//2
        while l<=h:
            val = s(m)
            if val-target<0:
                l = m+1
                m = (l+h)//2
            elif val-target>0:
                h = m-1
                m = (l+h)//2
            else:
                return m
        v1 = s(l)
        v2 = s(h)
        
        if abs(v1-target)<abs(v2-target):
            return l
        elif abs(v1-target)>abs(v2-target):
            return h
        else:
            return min(l,h)
                
            
            
            
            
            
            
        
        
        
            
        
        
