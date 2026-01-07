
class Solution:
    
    def checkPerfectNumber(self, num: int) -> bool:
        if num&1==True:
            return False
        primes = [2, 3, 5, 7, 13, 17, 19]
        
        for x in primes:
            if (2**(x-1))*(2**x - 1)==num:
                return True
        return False
