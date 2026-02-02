class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        lim1 = len(nums1)
        lim2 = len(nums2)
        
        
            
        n1 = 0
        n2 = 0
        
        if lim1<=lim2:
            for x in nums1:
                nums2.append(x)
                n2=1
                nums2.sort()
        else:
            for x in nums2:
                nums1.append(x)
                n1=1
                nums1.sort()
                
        if lim1==0:
            n1 = 0
            n2 = 1
        elif lim2==0:
            n2 = 0
            n1 = 1
            
            
        l = lim1+lim2
        
        if l%2==0:
            if n1==1:
                return (nums1[l//2]+nums1[l//2 - 1])/2
            else:
                return (nums2[l//2]+nums2[l//2 - 1])/2
        else:
            if n1==1:
                return (nums1[l//2])
            else:
                return (nums2[l//2])
        
        
