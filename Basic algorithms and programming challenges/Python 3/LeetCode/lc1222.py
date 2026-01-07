from math import sqrt
class Solution:
    def p(self, l: List[int]) -> float:
        return sqrt((l[0]-l[1])**2 + (l[2]-l[3])**2)
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        k = king
        f = []
        pos_dru = []
        pos_dlu = []
        pos_drd = []
        pos_dld = []
        
        pos_vu = []
        pos_vd = []
        
        pos_hl = []
        pos_hr = []
        
        for x in queens:
            if x[0]==k[0]:
                if x[1]>k[1]:
                    pos_hr.append(x)
                else:
                    pos_hl.append(x)
                    
            if x[1]==k[1]:
                if x[0]<k[0]:
                    pos_vu.append(x)
                else:
                    pos_vd.append(x)
            slope = 1.1
            
            if k[1]-x[1]!=0 and k[0]-x[0]!=0:        
                
                slope = (k[0]-x[0])/(k[1]-x[1])
                
            if abs(slope).is_integer() and abs(slope)==1:
                if x[0]>k[0] and x[1]>k[1]:
                    pos_drd.append(x)
                elif x[0]>k[0] and x[1]<k[1]:
                    pos_dld.append(x)
                elif x[0]<k[0] and x[1]>k[1]:
                    pos_dru.append(x)
                else:
                    pos_dlu.append(x)
        
        f = []
        a = -1
        mn = 100000
        for x in pos_hr:
            t = self.p([k[1],x[1],k[0],x[0]])
            if t<mn:
                print(x)
                mn = t
                a = x
        if a!=-1:
            f.append(a)
            
        a = -1
        mn = 100000
        for x in pos_hl:
            t = self.p([k[1],x[1],k[0],x[0]])
            if t<mn:
                mn = t
                a = x
        if a!=-1:
            f.append(a)
            
        a = -1
        mn = 100000
        for x in pos_vd:
            t = self.p([k[1],x[1],k[0],x[0]])
            if t<mn:
                mn = t
                a = x
        if a!=-1:
            f.append(a)
            
        a = -1
        mn = 100000
        for x in pos_vu:
            t = self.p([k[1],x[1],k[0],x[0]])
            if t<mn:
                mn = t
                a = x
        if a!=-1:
            f.append(a)
            
        a = -1
        mn = 100000
        for x in pos_drd:
            t = self.p([k[1],x[1],k[0],x[0]])
            if t<mn:
                mn = t
                a = x
        if a!=-1:
            f.append(a)
            
            
        a = -1
        mn = 100000
        for x in pos_dru:
            t = self.p([k[1],x[1],k[0],x[0]])
            if t<mn:
                mn = t
                a = x
        if a!=-1:
            f.append(a)
            
        a = -1
        mn = 100000
        for x in pos_dld:
            t = self.p([k[1],x[1],k[0],x[0]])
            if t<mn:
                mn = t
                a = x
        if a!=-1:
            f.append(a)    
            
        a = -1
        mn = 100000
        for x in pos_dlu:
            t = self.p([k[1],x[1],k[0],x[0]])
            if t<mn:
                mn = t
                a = x
        if a!=-1:
            f.append(a)
        return f
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
        
        
        
                    
        
            
