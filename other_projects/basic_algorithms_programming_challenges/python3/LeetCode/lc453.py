class Solution:
    def minMoves(self, nums: List[int]) -> int:
        
        
        k = list(set(nums))
        k.sort()
        
        d = dict()
        for x in nums:
            try:
                d[x]+=1
            except:
                d[x]=1
         
        mn = min(k)
        mx = max(k)
    
        nums.sort()
        ###print(nums)
        
        t = (mx-mn)*nums.count(mx)
        del k[k.index(mx)]
        del d[mx]
        
        for x in d:
            t+=abs(mn-x)*d[x]
        return t
