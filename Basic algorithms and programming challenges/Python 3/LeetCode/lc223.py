class Solution:
    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
        
        
        l1 = [[A,C],[E,G]]
        
        l1.sort(key=lambda x: x[0])
        
        l2 = [[B,D],[F,H]]
        
        l2.sort(key=lambda x: x[0])
        
        intx = [max(l1[0][0],l1[1][0]),min(l1[0][1],l1[1][1])]
        inty = [max(l2[0][0],l2[1][0]),min(l2[0][1],l2[1][1])]
        
        if intx[0]<intx[1] and inty[0]<inty[1]:
            return ((C-A)*(D-B)) + ((G-E)*(H-F)) - (intx[1]-intx[0])*(inty[1]-inty[0])
        else:
            return ((C-A)*(D-B)) + ((G-E)*(H-F))
        
        
        
