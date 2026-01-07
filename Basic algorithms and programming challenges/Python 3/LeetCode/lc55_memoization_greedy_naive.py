'''
Will recursively check each each possible set of jumps, returning true if from
a given position we can reach the end (backtracking)
the function will pass each jump from the start up to the maximum jump from the start
into itself which will then take the index arrived at as the start and repeat, eventually
returning true if by doing this we reach the end, or false if the given index we are
at exhausts its possible jumps without returning true
-can potentially take a very long time

class Solution:
    def backtrack(self, index, nums,lim):
        if index==lim-1:
            return True
        
        max_jump = min([index+nums[index],lim-1])
        
        i = index+1
        while i<=max_jump:
            if self.backtrack(i,nums,lim)==True:
                return True
            
            i+=1
        return False
        
    def canJump(self, nums: List[int]) -> bool:
        return self.backtrack(0,nums,len(nums))
'''
'''
using memoization table to limit the number of calls

class Solution:
    def __init__(self):
        self.memo = []
    def backtrack(self, index, nums,lim):
        
        if self.memo[index]!=0:
            return self.memo[index]==1
            
        
        max_jump = min([index+nums[index],lim-1])
        
        i = index+1
        while i<=max_jump:
            if self.backtrack(i,nums,lim)==True:
                self.memo[index]=1
                
                return True
            
            i+=1
        self.memo[index]=-1
        return False
        
    def canJump(self, nums: List[int]) -> bool:
        
        lim = len(nums)
        self.memo = [0 for i in range(0,lim-1)]
        self.memo.append(1)
        return self.backtrack(0,nums,lim)
    '''
class Solution:
    '''
    takes advantage of the fact that if a spot can reach the end,
    then we can call that spot the end
    '''
    def canJump(self, nums: List[int]) -> bool:
        
        toend = len(nums)-1
        
        i = toend
        while i>=0:
            if i+nums[i]>=toend:
                toend=i
            i-=1
        return toend==0



