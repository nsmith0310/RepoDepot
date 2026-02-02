class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        
        if len(coordinates)<2:
            return False
        
        coordinates.sort(key=lambda x: x[0])
        
        print(coordinates)
        v = []
        h = []
        for x in coordinates:
            v.append(x[1])
            h.append(x[0])
        if len(list(set(v)))==1:return True
        if len(list(set(h)))==1:return True
        
        d = []
        
        
        i = 0
        while i<len(coordinates)-1:
            num = (coordinates[i+1][1]-coordinates[i][1])
            den = (coordinates[i+1][0]-coordinates[i][0])
            if num ==0:
                d.append(0)
            elif den == 0:
                d.append('x')
            else:
                d.append(num/den)
            i+=1
        print(d)
        if len(list(set(d)))==1:return True
        return False
