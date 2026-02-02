class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        l = nums
        i = 0
        l2=[]
        while i<len(l):
            c=0
            for x in l:
                if x!=l[i]:
                    if x<l[i]:
                        c+=1
            l2.append(c)
            i+=1
        return l2
