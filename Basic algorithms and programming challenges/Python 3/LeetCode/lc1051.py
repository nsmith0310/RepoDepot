class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        l1 = heights
        l2 = list(map(str,l1))
        l1.sort()
        l2 = list(map(int,l2))
        i = 0
        c = 0
        while i<len(l1):
            if l1[i]!=l2[i]:
                c+=1
            i+=1
        return c
