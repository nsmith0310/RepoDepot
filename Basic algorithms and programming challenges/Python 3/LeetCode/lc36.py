class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        i = 0
        while i<len(board):
            j = 0
            while j<len(board):
                if board[i][j]==".":board[i][j]="0"
                j+=1
            i+=1
            
        s1 = [board[0][0:3],board[1][0:3],board[2][0:3]]
        s2 = [board[0][3:6],board[1][3:6],board[2][3:6]]   
        s3 = [board[0][6:9],board[1][6:9],board[2][6:9]]
        
        s4 = [board[3][0:3],board[4][0:3],board[5][0:3]]
        s5 = [board[3][3:6],board[4][3:6],board[5][3:6]]   
        s6 = [board[3][6:9],board[4][6:9],board[5][6:9]]
        
        s7 = [board[6][0:3],board[7][0:3],board[8][0:3]]
        s8 = [board[6][3:6],board[7][3:6],board[8][3:6]]   
        s9 = [board[6][6:9],board[7][6:9],board[8][6:9]]
        
        sq = [s1,s2,s3,s4,s5,s6,s7,s8,s9]
        
        for x in sq:
            tmp = []
            for y in x:
                for z in y:
                    if z!='0':tmp.append(z)
            if len(list(set(tmp)))!=len(tmp): return False
        
        
        
        i = 0
        while i<len(board):
            tmp = []
            for x in board[i]:
                if x!='0':tmp.append(x)
            if len(list(set(tmp)))!=len(tmp): return False
            i+=1
        
        c = 0
        while c<len(board):
            arr = [board[0][c],board[1][c],board[2][c],board[3][c],board[4][c],board[5][c],board[6][c],board[7][c],board[8][c]]
            
            tmp = []
            for x in arr:
                if x!='0':tmp.append(x)
            if len(list(set(tmp)))!=len(tmp): 
                return False
            c+=1
            
        return True
        
        
        
        
        
        
