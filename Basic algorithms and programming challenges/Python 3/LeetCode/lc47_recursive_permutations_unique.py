class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if len(nums)==0:
            return []
        elif len(nums)==1:
            return [nums]
        else:
            l = []
            i = 0
            while i<len(nums):
                prepend = nums[i]
                
                recur = nums[:i]+nums[i+1:]
                
                for x in self.permuteUnique(recur):
                    z = [prepend]+x
                    if z not in l:
                        l.append(z)
                    
                i+=1
            return l
