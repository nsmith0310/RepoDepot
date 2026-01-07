class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i = len(nums1)-1
        while i >=m:
            del nums1[i]
            
            i-=1
        for x in nums2:
            nums1.append(x)
        nums1.sort()
