class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        rook=[]
        bish=[]
        pawn=[]
        
        i = 0
        while i<len(board):
            j = 0
            while j<len(board[i]):
                if board[i][j]=="R":
                    rook = [i,j]
                j+=1
            i+=1
            
        i = 0
        while i<len(board):
            j = 0
            while j<len(board[i]):
                
                if board[i][j]=="B":
                    if i==rook[0] or j==rook[1]:
                        bish.append([i,j])
                elif board[i][j]=="p":
                    if i==rook[0] or j==rook[1]:
                        pawn.append([i,j])
                j+=1
            i+=1
            
        
        up = []
        down = []
        left = []
        right = []
        
        mnu = 10
        mnd = 10
        mnl = 10
        mnr = 10
        
        for x in pawn:
            if abs(rook[1]-x[1])<mnr and x[1]>rook[1]:
                mnr=abs(rook[1]-x[1])
                right = x
            if abs(rook[1]-x[1])<mnl and x[1]<rook[1]:
                mnl=abs(rook[1]-x[1])
                left = x
            if abs(rook[0]-x[0])<mnu and x[0]<rook[0]:
                mnu=abs(rook[0]-x[0])
                up = x
            if abs(rook[0]-x[0])<mnd and x[0]>rook[0]:
                mnd=abs(rook[0]-x[0])
                down = x
        
        br=0
        bl=0
        bu=0
        bd=0
        c = 0
        for x in bish:
            if right!=[]:
                if abs(rook[1]-x[1])<mnr and x[1]>rook[1] and x[1]<right[1]:
                    br=1
            if left!=[]:
                if abs(rook[1]-x[1])<mnl and x[1]<rook[1] and x[1]>left[1]:
                    bl=1
            if up!=[]:
                if abs(rook[0]-x[0])<mnu and x[0]<rook[0] and x[0]>up[0]:
                    bu=1
            if down!=[]:
                if abs(rook[0]-x[0])<mnd and x[0]>rook[0] and x[0]<down[0]:
                    bd=1
        
        
        total = 0
        if up!=[] and bu!=1:
            total+=1
        if down!=[] and bd!=1:
            total+=1
        if left!=[] and bl!=1:
            total+=1
        if right!=[] and br!=1:
            total+=1
        return total
        
        
        
            
        
        
                
            
            
            
            
            
            
            
            
            
            
