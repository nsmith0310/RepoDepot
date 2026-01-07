class Solution:
    def findLucky(self, arr: List[int]) -> int:
        l = list(set(arr))
        
        m = []
        for x in l:
            if arr.count(x)==x:
                m.append(x)
        if m==[]:return -1
        else:return max(m)
