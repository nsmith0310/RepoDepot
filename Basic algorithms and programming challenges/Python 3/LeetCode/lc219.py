class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        f = [0 for i in range(0,len(nums))]
        
        tmp = []
        i = 0
        while i<len(nums):
            tmp.append([nums[i],i])
            i+=1
        tmp.sort(key=lambda x: x[0])
        
        i = 0
        while i<len(tmp)-1:
            if tmp[i][0]==tmp[i+1][0]:
                tmp[i].append(tmp[i+1][1])
                del tmp[i+1]
                i-=1
            i+=1
        
        ###print(tmp)
        for x in tmp:
            i = 1
            while i<len(x)-1:
                j = i+1
                while j<len(x):
                    if abs(x[i]-x[j])<=k:
                        return True
                    j+=1
                i+=1
        return False
