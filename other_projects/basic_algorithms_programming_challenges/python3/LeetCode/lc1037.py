class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        
        slope = 0
        
        line = 0
        
        
        a = points[0]
        b = points[1]
        c = points[2]
        if a==b==c:
            return False
        if a==b or b==c or a==c:
            return False
        
        
        
        if a[1]==b[1]==c[1]:return False
        if a[0]==b[0]==c[0]:return False
        
        
        
        ba = 0.0
        ca = 0.0
        cb = 0.0
        
        
        if abs(b[0]-a[0])!=0:
            ba = abs(b[1]-a[1])/abs(b[0]-a[0])
        if abs(c[0]-a[0])!=0:
            ca = abs(c[1]-a[1])/abs(c[0]-a[0])
        if abs(c[0]-b[0])!=0:
            cb = abs(c[1]-b[1])/abs(c[0]-b[0])
        print(ba,ca,cb)
        
        if ba!=ca or ca!=cb or ca!=ba:return True
        return False
