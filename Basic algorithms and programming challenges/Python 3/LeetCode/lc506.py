class Solution:
    def findRelativeRanks(self, nums: List[int]) -> List[str]:
        l = [x for x in nums]
        l.sort(reverse=True)
        
        m = []
        i = 0
        while i<len(nums):
            m.append([nums[i],l.index(nums[i])])
            i+=1
        
        final = []
        i = 0
        while i<len(m):
            if m[i][1]==0:
                final.append("Gold Medal")
            elif m[i][1]==1:
                final.append("Silver Medal")
            elif m[i][1]==2:
                final.append("Bronze Medal")
            else:
                final.append(str(m[i][1]+1))
            i+=1
        return final
