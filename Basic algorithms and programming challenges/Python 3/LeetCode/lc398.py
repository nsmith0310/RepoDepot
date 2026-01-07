from random import randint as r
class Solution:

    def __init__(self, nums: List[int]):
        self.dic = dict()
        self.l = dict()
        
        i = 0
        while i<len(nums):
            try:
                self.dic[nums[i]].append(i)
                self.l[nums[i]]+=1
            except:
                self.dic[nums[i]]=[i]
                self.l[nums[i]]=0
            i+=1

    def pick(self, target: int) -> int:
        return self.dic[target][r(0,self.l[target])]


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
