class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        l = []
        for x in nums:
            if x>0:
                l.append(x)
        if l==[]:return 1
        l.sort()
        if l[0]!=0:
            l.insert(0,0)
        
        
        i = 0
        while i<len(l)-1:
            if l[i]+1<l[i+1]:
                return l[i]+1
            i+=1
        return l[-1]+1
