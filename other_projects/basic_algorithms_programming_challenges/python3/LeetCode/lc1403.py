class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        k = sum(nums)
        m = []
        t = 0
        while t<=k:
            p = max(nums)
            del nums[nums.index(p)]
            t+=p
            k-=p
            m.append(p)
        m.sort(reverse=True)
        return m
