class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        length = len(nums)
        
        l = 0
        h = length -1
        m = (length)//2
        
        while l<=h:
            t = nums[m]
            if t<target:
                l = m+1
                m = (l+h)//2
            elif t>target:
                h = m-1
                m = (l+h)//2
            elif t==target:
                return m
        return -1
