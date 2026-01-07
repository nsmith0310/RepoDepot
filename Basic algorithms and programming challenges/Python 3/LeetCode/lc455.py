class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        c = 0
        g.sort(reverse=True)
        s.sort(reverse=True)
        
        i = 0
        while i<len(g):
            greed = g[i]
            j = 0
            while j<len(s):
                if greed<=s[j]:
                    c+=1
                    del s[j]
                    break
                j+=1
            i+=1
        return c
