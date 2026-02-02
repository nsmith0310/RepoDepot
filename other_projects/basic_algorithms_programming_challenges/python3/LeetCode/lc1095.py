# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        
        
        lim = mountain_arr.length()
        
        l = 0
        h = lim-1
        m = (l+h)//2
        
        
        while l<=h:
            if l==0 and m==0 and h==1:
                m = h
                break
            t = mountain_arr.get(m)
            a = mountain_arr.get(m-1)
            c = mountain_arr.get(m+1)
            
            if t>a and t>c:
                if t==target:
                    return m
                peak = m
                break
            elif t<c:
                l = m+1
                m = (l+h)//2
            elif t<a:
                h = m-1
                m = (l+h)//2
        
        l = 0
        h = m-1
        mid = (l+h)//2
        
        while l<=h:
            t = mountain_arr.get(mid)
            if t==target:
                return mid
            elif t<target:
                l = mid+1
                mid = (l+h)//2
            else:
                h = mid-1
                mid = (l+h)//2
                
        l = m 
        h = lim-1
        mid = (l+h)//2
        while l<=h:
            t = mountain_arr.get(mid)
            if t==target:
                return mid
            elif t>target:
                l = mid+1
                mid = (l+h)//2
            else:
                h = mid-1
                mid = (l+h)//2
                
        return -1
                
