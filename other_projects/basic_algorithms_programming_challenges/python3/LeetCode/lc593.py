from itertools import combinations as c

class Solution:
    def e(self,p1,p2):
        return ((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)**.5
    
    
        
    
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        nums = list(c([p1,p2,p3,p4],2))
        
        dis = []
        
        for x in nums:
            dis.append(self.e(x[0],x[1]))
        
        d2 = list(set(dis))
        
        if len(d2)!=2:
            return False
        
        counts=[]
        
        for x in d2:
            counts.append(dis.count(x))
        counts.sort()
        return counts==[2,4]
        
