from itertools import combinations as c

class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        l = c(points,3)
        mx = 0
        for x in l:
            p1 = x[0]
            p2 = x[1]
            p3 = x[2]
            a = (p1[0]*(p2[1]-p3[1]) + p2[0]*(p3[1]-p1[1]) + p3[0]*(p1[1]-p2[1]))/2
            
            if abs(a)>mx:
                mx = abs(a)
        return mx
