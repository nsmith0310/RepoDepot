class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        final=[]
        i = 0
        while i<len(nums1):
            t=0
            j = nums2.index(nums1[i])+1
            while j<len(nums2):
                if nums2[j]>nums1[i]:
                    t=1
                    final.append(nums2[j])
                    break
                j+=1
            if t==0:
                final.append(-1)
            i+=1
            
        return final
               
