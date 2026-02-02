class Solution:
    def e(self, p1, p2):
        return ((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)**.5
    
    def m(self,p1,p2):
        return abs(p1[0]-p2[0])+abs(p1[1]-p2[1])
    
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        
        c = 0
        
        i = 0
        while i<len(points):
            d = dict()
            j =0
            while j<len(points):
                if j!=i:
                    dis = self.e(points[i],points[j])
                    key = 'n'.join([str(points[i][0]),str(points[i][1])])
                
                    
                    try:
                        d[dis]+=1
                    except:
                        d[dis]=1
                j+=1
            
            for x in d:
                val = d.get(x)
                c+= val*(val-1)
            i+=1
        
        return c
                    
