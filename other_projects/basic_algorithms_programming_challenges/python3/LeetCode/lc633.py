from math import floor, sqrt
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        
        for x in range(0,floor(sqrt(c))+1):
            if sqrt(c-x**2).is_integer(): return True
        return False
