class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        c=0
        l = list(map(str,nums))
        for x in l:
            if len(x)&1==False:
                c+=1
        return c
