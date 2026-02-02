class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        
        l = list(set(nums))
        l.sort(reverse=True)
        if len(l)<3:
            return max(l)
        else:
            return l[2]
