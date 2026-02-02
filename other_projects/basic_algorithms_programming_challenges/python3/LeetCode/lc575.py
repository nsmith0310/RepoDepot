class Solution:
    def distributeCandies(self, candies: List[int]) -> int:
        t = list(set(candies))
        
        mx = 0
        lim = len(candies)//2
        
        i = 0
        while i<len(t):
            if lim==0:
                break
            else:
                mx+=1
                lim-=1
            i+=1
            
        return mx
                
                
            
                
