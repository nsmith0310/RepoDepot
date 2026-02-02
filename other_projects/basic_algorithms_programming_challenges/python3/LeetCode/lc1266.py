class Solution:
        
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        t = 0
        lim = len(points)
        if lim==1:return 0
        
        i = 0
        while i<lim-1:
            p1 = points[i]
            p2 = points[i+1]
            u = [x for x in p1]
            v = [x for x in p2]
            
            tmp = 0
            
            if p1[0]==p2[0]:
                t+=abs(p1[1]-p2[1])
            elif p1[1]==p2[1]:
                t+=abs(p1[0]-p2[0])
            
            
            elif p1[0]<=p2[0] and p1[1]<=p2[1]:
                
                while 1!=-1:
                    p1[0]+=1
                    p1[1]+=1
                    
                    tmp+=1
                    if p1[0]==p2[0] or p1[1]==p2[1]:
                        break
                if p1!=p2:
                    if p1[0]!=p2[0]:
                        tmp+=abs(p1[0]-p2[0])
                        
                    else:
                        tmp+=abs(p1[1]-p2[1])
                        
            elif p1[0]<=p2[0] and p1[1]>=p2[1]:
                if abs(p1[0]-p2[0])>abs(p1[1]-p2[1]):
                    while 1!=-1:
                        p1[0]+=1
                        p1[1]-=1
                        tmp+=1
                        
                        if p1[0]==p2[0] or p1[1]==p2[1]:
                            break
                    if p1!=p2:
                        if p1[0]!=p2[0]:
                            tmp+=abs(p1[0]-p2[0])
                        else:
                            tmp+=abs(p1[1]-p2[1])
                else:
                    
                    while 1!=-1:
                        p1[0]+=1
                        p1[1]-=1
                        tmp+=1
                        if p1[0]==p2[0] or p1[1]==p2[1]:
                            break
                                  
                    if p1!=p2:
                        if p1[0]!=p2[0]:
                            tmp+=abs(p1[0]-p2[0])
                        else:
                            tmp+=abs(p1[1]-p2[1])      
            
            elif p1[0]>=p2[0] and p1[1]>=p2[1]:
                
                while 1!=-1:
                    p1[0]-=1
                    p1[1]-=1
                    
                    tmp+=1
                    if p1[0]==p2[0] or p1[1]==p2[1]:
                        
                        break
                if p1!=p2:
                    if p1[0]!=p2[0]:
                        tmp+=abs(p1[0]-p2[0])
                    else:
                        tmp+=abs(p1[1]-p2[1])
                
            elif p1[0]>=p2[0] and p1[1]<=p2[1]:
                if abs(p1[0]-p2[0])>abs(p1[1]-p2[1]):
                    while 1!=-1:
                        p1[0]-=1
                        p1[1]+=1
                        tmp+=1
                        
                        if p1[0]==p2[0] or p1[1]==p2[1]:
                            break
                    if p1!=p2:
                        if p1[0]!=p2[0]:
                            tmp+=abs(p1[0]-p2[0])
                        else:
                            tmp+=abs(p1[1]-p2[1])
                else:
                    while 1!=-1:
                        p1[0]-=1
                        p1[1]+=1
                        tmp+=1
                        if p1[0]==p2[0] or p1[1]==p2[1]:
                            break
                    if p1!=p2:
                        if p1[0]!=p2[0]:
                            tmp+=abs(p1[0]-p2[0])
                        else:
                            tmp+=abs(p1[1]-p2[1])      
            
            
            if u!=v:
                t+=tmp
            
            i+=1
        return t
