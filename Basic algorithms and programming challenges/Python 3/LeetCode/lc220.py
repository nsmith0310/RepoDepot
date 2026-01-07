class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        
        
        
        lim = len(nums)
        
        l = [[nums[i],i] for i in range(0,lim)]
        l.sort(key=lambda x: x[0])
        
        i = 0
        while i<len(l)-1:
            j = i+1
            while j<len(l):
                if abs(l[i][0]-l[j][0])>t:
                    break
                if abs(l[i][1]-l[j][1])<=k:return True
                j+=1
            i+=1
        return False
