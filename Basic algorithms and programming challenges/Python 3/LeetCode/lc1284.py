from copy import deepcopy
class Solution:
    def minFlips(self, mat: List[List[int]]) -> int:
        
        
        lim1 = len(mat)
        lim2 = len(mat[0])
        comp = [[0 for i in range(0,lim2)] for j in range(0,lim1)]
        mn = 9999999999999999999
        
        f = []
        tmp = [[mat,0]]
        
        while 1!=-1:
            t =0
            for x in tmp:
                
                if x[0]==comp:
                    if x[1]<mn:
                        
                        mn = x[1]
                else:
                    reset = deepcopy(x[0])
                
                    i = 0
                    while i<lim1:
                        j = 0
                        while j<lim2:
                            if reset[i][j]==1:
                                reset[i][j]=0
                            else:
                                reset[i][j]=1
                            if i>0:
                                if reset[i-1][j]==1:
                                    reset[i-1][j]=0
                                else:
                                    reset[i-1][j]=1
                            if i<lim1-1:
                                if reset[i+1][j]==1:
                                    reset[i+1][j]=0
                                else:
                                    reset[i+1][j]=1
                            if j>0:
                                if reset[i][j-1]==1:
                                    reset[i][j-1]=0
                                else:
                                    reset[i][j-1]=1
                            if j<lim2-1:
                                if reset[i][j+1]==1:
                                    reset[i][j+1]=0
                                else:
                                    reset[i][j+1]=1
                        
                            if reset not in f:
                                t=1
                                tmp.append([reset,x[1]+1])
                                f.append(reset)
                            reset = deepcopy(x[0])
                            j+=1
                        i+=1
            if t==0:
                break
        if mn==9999999999999999999:
            return -1
        else:
            return mn
                        
                        
                    
                    
                        
        
