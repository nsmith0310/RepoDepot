class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        
        l = list(set(nums))
        l.sort()
        
        freq = []
        
        for x in l:
            freq.append([x,nums.count(x)])
        freq.sort(key=lambda x: x[1])
        freq = freq[::-1]
        
        mx = freq[0][1]
        n = [freq[0][0]]
        
        i = 1
        while i<len(freq):
            if freq[i][1]!=mx:
                break
            n.append(freq[i][0])
            i+=1
        
        l2 = [[] for x in n]
        
        
        i = 0
        while i<len(nums):
            try:
                l2[n.index(nums[i])].append(i)
            except:
                pass
            i+=1
            
        mn = 9999999999
        
        for x in l2:
            
            if x[-1]-x[0]+1 <mn:
                mn = x[-1]-x[0]+1
        
        return mn
            
