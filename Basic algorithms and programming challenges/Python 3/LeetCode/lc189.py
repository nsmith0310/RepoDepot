class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 1
        while i<=k:
            
            l = nums[-1]
            del nums[-1]
            nums.insert(0,l)
            i+=1
                
