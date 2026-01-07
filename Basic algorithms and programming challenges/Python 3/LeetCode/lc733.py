class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        q = [[sr,sc]]
        c = 0
        
        i = 0
        while q!=[]:
            for x in q:
            
            
                if x[0]!=0:
                    if image[x[0]-1][x[1]]==image[x[0]][x[1]]:
                        if image[x[0]-1][x[1]]!=newColor:
                            q.append([x[0]-1,x[1]])
                    
                if x[0]!=len(image)-1:
                    if image[x[0]+1][x[1]]==image[x[0]][x[1]]:
                        if image[x[0]+1][x[1]]!=newColor:
                            q.append([x[0]+1,x[1]])
                    
                if x[1]!=0:
                    if image[x[0]][x[1]-1]==image[x[0]][x[1]]:
                        if image[x[0]][x[1]-1]!=newColor:
                            q.append([x[0],x[1]-1])
                    
                if x[1]!=len(image[0])-1:
                    if image[x[0]][x[1]+1]==image[x[0]][x[1]]:
                        if image[x[0]][x[1]+1]!=newColor:
                            q.append([x[0],x[1]+1])
                
                image[x[0]][x[1]]=newColor
            
                del q[q.index(x)]
            
        return image
