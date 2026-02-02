from math import ceil,floor

class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def div(v):
            t = 0
            for x in nums:
                t+=ceil(x/v)
            return t
        
        
        l = 1
        h = max(nums)
        
        while l<=h:
            m = (l+h)//2
            val = div(m)
            
            if threshold-val>=0:
                h = m-1
            elif threshold-val<=0:
                l = m+1
        if l==0:return h
        if h==0:return l
        v1 = div(l)
        v2 = div(h)
        
        if v1>threshold:
            return h
        elif v2>threshold:
            return l
        else:
            return min(l,h)
