class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        if r*c!=len(nums)*len(nums[0]):
            return nums
        if r == len(nums) and c==len(nums[0]):
            return nums
        
        new = [[] for i in range(1,r+1)]
        
        
        l = []
        for x in nums:
            for y in x:
                l.append(y)
                
        
        i = 0
        col = 1
        row = 1
        while i<len(l):
            if len(new[row-1])<c:
                
                new[row-1].append(l[i])
            else:
                row+=1
                new[row-1].append(l[i])
            i+=1
        return new
                
            
