class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        
        xvals = [rec1[0],rec1[2]]
        yvals = [rec1[1],rec1[3]]
        
        avals = [rec2[0],rec2[2]]
        bvals = [rec2[1],rec2[3]]
        
        xvals.sort()
        yvals.sort()
        avals.sort()
        bvals.sort()
        
        print(xvals)
        print(avals)
        
        print(yvals)
        print(bvals)
        
        x = 0
        y = 0
        t1 = 0
        t2 = 0
        
        if xvals[0]>=avals[0] and xvals[0]<=avals[1]:
            t1=1
        elif xvals[0]<=avals[0] and xvals[1]>=avals[1]:
            t1=1
        elif xvals[1]>=avals[0] and xvals[1]<=avals[1]:
            t1=1
        elif xvals[0]>=avals[0] and xvals[1]<=avals[1]:
            t1=1
            
        if xvals==avals:
            x = 1
            
        if yvals[0]>=bvals[0] and yvals[0]<=bvals[1]:
            t2=1
        elif yvals[0]<=bvals[0] and yvals[1]>=bvals[1]:
            t2=1
        elif yvals[1]>=bvals[0] and yvals[1]<=bvals[1]:
            t2=1
        elif yvals[0]>=bvals[0] and yvals[1]<=bvals[1]:
            t2=1
            
        if yvals==bvals:
            y = 1
        if x==y==1:
            return False
        
        
        if xvals[1]==avals[0] or xvals[0]==avals[1]:
            return False
        if yvals[1]==bvals[0] or yvals[0]==bvals[1]:
            return False
        
        
        return t1==t2==1 
        
        
        
        
        
        
