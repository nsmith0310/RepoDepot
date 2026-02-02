class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        
        points.sort(key=lambda x: x[1])
        
        i = 0
        while i<len(points)-1:
            
            l = [points[i],points[i+1]]
            l.sort(key=lambda x: x[0])
            l2 = [max(l[0][0],l[1][0]),min(l[0][1],l[1][1])]
            if l2[0]<=l2[1]:
                del points[i+1]
                if i!=0:i-=1
            else:
                i+=1
        
        return len(points)
        
