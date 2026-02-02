class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        l=[]
        t = list(set(nums))
        for x in t:
            if nums.count(x)!=2:
                l.append(x)
        return l
