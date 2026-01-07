class Solution:
    def findLHS(self, nums: List[int]) -> int:
        
        nums.sort()
        l = list(set(nums))
        l.sort()
        l2=[]
        i = 0
        while i<len(l)-1:
            if l[i]==l[i+1]-1:
                l2.append([l[i],l[i+1]])
            i+=1
            
        mx = 0
        for x in l2:
            n1 = nums.count(x[0])
            n2 = nums.count(x[1])
            if n1+n2>mx:
                mx = n1+n2
        return mx
                           
