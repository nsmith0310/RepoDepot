from math import sqrt

class Solution:
    def e(self, l: List[int]) -> int:
        return sqrt((l[1])**2 + (l[0])**2)
        
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        l = [[x, self.e(x)] for x in points]
        
        l.sort(key = lambda x: x[1])
        
        f=[]
        i = 0
        while i<K:
            f.append(l[i][0])
            i+=1
        return f
