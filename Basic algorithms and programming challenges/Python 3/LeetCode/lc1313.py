class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        l = nums
        final=[]
        i = 0
        while i<len(l)-1:
            n1=l[i]
            n2=l[i+1]
            j=0
            while j<n1:
                final.append(n2)
                j+=1
            i+=2
        return final
