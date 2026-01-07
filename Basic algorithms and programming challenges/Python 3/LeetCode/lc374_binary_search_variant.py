# The guess API is already defined for you.
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:
from math import floor,ceil
class Solution:
    def guessNumber(self, n: int) -> int:
        l = 0
        h = n -1
        m = (n)//2
        
        while l<=h:
            t = m
            if guess(t)==1:
                l = m+1
                m = (l+h)//2
            elif guess(t)==-1:
                h = m-1
                m = (l+h)//2
            elif guess(t)==0:
                return t
        return l
                    
                
        
