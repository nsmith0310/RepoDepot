from itertools import combinations as c

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        
        nums = [1,2,3,4,5,6,7,8,9]
        
        f= []
        
        pos = list(c(nums,k))
        
        for x in pos:
            if sum(x)==n:
                f.append(list(x))
                
        return f
        
