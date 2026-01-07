class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        l1 = (set(nums1))
        l2 = (set(nums2))
        
        d1 = l1-l2
        
        
        s1 = l1-d1
    
        c1 = [[x,nums1.count(x)] for x in s1]
        c2 = [[x,nums2.count(x)] for x in s1]
        f = []
        i = 0
        while i<len(c1):
            if c1[i][1]<c2[i][1]:
                count = c1[i][1]
            else:
                count = c2[i][1]
            k = 0
            while k<count:
                f.append(c1[i][0])
                k+=1
            i+=1
        return f
        
