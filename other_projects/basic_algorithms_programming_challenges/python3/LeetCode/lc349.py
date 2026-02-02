class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        diffa = (set(nums1)-set(nums2))
        diffb = (set(nums2)-set(nums1))
        
        coma = list(set(nums1)-diffa)
        comb = list(set(nums2)-diffb)
        
        l = []
        for x in coma:
            l.append(x)
        for x in comb:
            l.append(x)
            
        return list(set(l))
