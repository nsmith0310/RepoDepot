class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l = []
        try:
            l.append(nums.index(target))
            nums.sort(reverse=True)
            k = nums.index(target)
            l.append(len(nums)-1-k)
            return l
                
        except:
            return [-1,-1]
