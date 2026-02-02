class Solution:
    def reconstructMatrix(self, upper: int, lower: int, colsum: List[int]) -> List[List[int]]:
        
        top = [0 for x in range(0,len(colsum))]
        bottom  = [0 for x in range(0,len(colsum))]
        
        c = 0
        i = 0
        while i<len(colsum):
            if colsum[i]==2:
                upper-=1
                lower-=1
                top[i]=1
                bottom[i]=1
            elif colsum[i]==1:
                c+=1
            i+=1
        
        i=0
        while i<len(top):
            if upper >0:
                if colsum[i]==1 and top[i]!=1:
                    top[i]=1
                    upper-=1
                    c-=1
            else:
                if lower >0 and colsum[i]==1 and bottom[i]!=1:
                    bottom[i]=1
                    lower-=1
                    c-=1
            
            i+=1
        
        if upper!=0 or lower!=0 or c!=0: return []
        return [top,bottom]
                
