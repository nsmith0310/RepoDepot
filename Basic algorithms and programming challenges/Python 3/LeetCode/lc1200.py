class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        l2 = arr
        l2.sort()
        mn=10**6 + 1
        i = 0
        while i<len(l2)-1:
            if abs(l2[i]-l2[i+1])<mn:
                mn=abs(l2[i]-l2[i+1])
            i+=1
        final=[]
        i = 0
        while i<len(l2)-1:
            if abs(l2[i]-l2[i+1])==mn:
                final.append([l2[i],l2[i+1]])
            i+=1
        return final
