class Solution:
    def minSteps(self, s: str, t: str) -> int:
        ls = list(set(s))
        l2s = [[x,s.count(x),t.count(x)] for x in ls]
        ###print(l2s)
        
        t = 0
        for x in l2s:
            if x[1]>=x[2]:
                t+=x[1]-x[2]
        return t
