from math import gcd
class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        
        f = []
        
        nums = [i for i in range(1,n+1)]
        
        i = 0
        while i<len(nums):
            j = 0
            while j<i:
                num = nums[j]
                num2 = nums[i]
                
                r = gcd(num,num2)
                num//=r
                num2//=r
                if num2<=n:
                    f.append(str(num)+"/"+str(num2))
                j+=1
            i+=1
        return list(set(f))
                
