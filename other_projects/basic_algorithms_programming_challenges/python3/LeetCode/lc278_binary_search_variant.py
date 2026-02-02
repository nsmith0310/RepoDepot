# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        
        
        
        l = 0
        h = n -1
        m = (n)//2
        
        while l<=h:
            t = m
            if isBadVersion(t)==False:
                l = m+1
                m = (l+h)//2
            elif isBadVersion(t)==True:
                h = m-1
                m = (l+h)//2
            
        return l
        
        
        
