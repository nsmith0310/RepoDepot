class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        mx = 0
        
        i = 0
        j = len(height)-1
        
        while i<=j:
            
            if height[i]<height[j]:
                tmp = height[i]*(j-i)
                if tmp>mx:mx = tmp
                i+=1
            else:
                tmp = height[j]*(j-i)
                if tmp>mx:mx = tmp
                j-=1
        return mx
                     
