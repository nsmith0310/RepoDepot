class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        
        if len(nums)%k!=0:return False
        nums.sort()
        
        
        while len(nums)>0:
            c = 0
            arr = [nums[0]]
            del nums[0]
            while c<k-1:
                
                try:
                    ind = nums.index(arr[-1]+1)
                    arr.append(nums[ind])
                    del nums[ind]
                    
                except:
                    return False
                c+=1
            
            arr=[]
        return True
