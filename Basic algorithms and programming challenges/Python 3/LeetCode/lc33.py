
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        length = len(nums)
        
        nums2 = [[nums[i],i] for i in range(0,length)]
        
        
        nums2.sort(key=lambda x: x[0])
                
        l = 0
        h = length -1
        m = (length)//2
        
        while l<=h:
            t = nums2[m]
            if t[0]<target:
                l = m+1
                m = (l+h)//2
            elif t[0]>target:
                h = m-1
                m = (l+h)//2
            elif t[0]==target:
                return t[1]
        return -1
