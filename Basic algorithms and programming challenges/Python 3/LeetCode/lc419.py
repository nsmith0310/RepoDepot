class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        if board == [[]]:return 0
        c = 0
        lim1 = len(board)
        lim2 = len(board[0])
        
        
        t = 0
        if board[0][0]=='X':
            c+=1
            if lim1>1:
                if board[1][0]=='X':
                    t = 1
                    k = 1
                    while k< lim1 and board[k][0]=='X':
                        board[k][0]='.'
                        k+=1
                
            if t==0:
                if lim2>1:
                    if board[0][1]=='X':
                        k = 1
                        while k< lim2 and board[0][k]=='X':
                            board[0][k]='.'
                            k+=1
                    
            board[0][0]='.'
                    
            
        
        
        
            
        
        
        
        
        
        
        
        
        
        
        i = 0
        while i<lim1:
                
            j = 0
            while j<lim2:
                if board[i][j]=="X":          
                    c+=1
                    
                    if i>0:
                        if board[i-1][j]=='X':
                            t = 1
                            k = i-1
                            while k>=0:
                                if board[k][j]=='X':
                                    board[k][j]="."
                                else:
                                    break
                                k-=1
                    
                    if i<len(board)-1:
                        if board[i+1][j]=='X':
                            t = 1
                            k = i+1
                            while k<lim1:
                                if board[k][j]=='X':
                                    board[k][j]="."
                                else:
                                    break
                                k+=1
                    
                    if j>0:
                        if board[i][j-1]=='X':
                            t = 1
                            k = j-1
                            while k>=0:
                                if board[i][k]=='X':
                                    board[i][k]="."
                                else:
                                    break
                                k-=1
                    
                    if j<len(board[i])-1:
                        if board[i][j+1]=='X':
                            t = 1
                            k = j+1
                            while k<lim2:
                                if board[i][k]=='X':
                                    board[i][k]="."
                                else:
                                    break
                                k+=1
                    
                j+=1
            i+=1
        return c
                        
                            
