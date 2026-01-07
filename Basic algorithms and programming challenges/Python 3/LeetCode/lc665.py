class Solution:
    def check(self, nums: List[int],ideal: List[int],num: int) -> bool:
        t=0
        f = ideal.index(num)
        del ideal[f]
        if nums==ideal:
            t=1
        ideal.insert(f,num)
        
        return t==1
    
    def checkPossibility(self, nums: List[int]) -> bool:
        ideal = [x for x in nums]
        ideal.sort()
        
        
        mx = len(nums)-1
        i = 0
        while i<len(nums):
            if i==0:
                p = nums[0]
                del nums[0]
                if self.check(nums,ideal,p)==True:
                    return True
                nums.insert(0,p)
            elif i!=mx:
                p = nums[i]
                del nums[i]
                if self.check(nums,ideal,p)==True:
                    return True
                nums.insert(i,p)
            else:
                p = nums[-1]
                del nums[-1]
                if self.check(nums,ideal,p)==True:
                    return True
            i+=1
        return False
                
        
            
            
