from math import sqrt,ceil
class Solution:
    def closestDivisors(self, num: int) -> List[int]:
        k = ceil(sqrt(num))
        
        while 1!=-1:
            if (num+1)%k==0:
                return [k,(num+1)//k]
            if (num+2)%k==0:
                return [k,(num+2)//k]
            k-=1
