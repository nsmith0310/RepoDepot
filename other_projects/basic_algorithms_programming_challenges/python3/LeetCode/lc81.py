class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        
        nums = list(set(nums))
        nums.sort()
        
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
                return True
        return False
