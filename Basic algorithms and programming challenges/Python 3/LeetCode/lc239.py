class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k==1:return nums
        
        f = []
        i = 0
        wind = nums[:k]
        f.append(max(wind))
        mx = max(wind)
        while i<len(nums)-k:
            
            if mx == wind[0]:
                del wind[0]
                wind.append(nums[i+k])
                mx = max(wind)
                f.append(mx)
            else:
                del wind[0]
                if nums[i+k]>mx:
                    mx = nums[i+k]
                f.append(mx)
                wind.append(nums[i+k])
            
            i+=1
        return f
