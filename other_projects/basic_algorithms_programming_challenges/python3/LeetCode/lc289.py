class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        l = [[0 for i in range(0,len(board[0]))] for j in range(0,len(board))]
        
        i = 0
        while i<len(board):
            j = 0
            while j<len(board[i]):
                ln = 0
                
                live = board[i][j]

                if i>0:
                    if board[i-1][j]==1:
                        ln+=1
                if i<len(board)-1:
                    if board[i+1][j]==1:
                        ln+=1
                if j>0:
                    if board[i][j-1]==1:
                        ln+=1
                if j<len(board[i])-1:
                    if board[i][j+1]==1:
                        ln+=1
                if i>0 and j>0:
                    if board[i-1][j-1]==1:
                        ln+=1
                if i>0 and j<len(board[i])-1:
                    if board[i-1][j+1]==1:
                        ln+=1
                if i<len(board)-1 and j>0:
                    if board[i+1][j-1]==1:
                        ln+=1
                if i<len(board)-1 and j<len(board[i])-1:
                    if board[i+1][j+1]==1:
                        ln+=1
                        
                if live==1 and ln==2 or ln==3:
                    l[i][j]=1
                elif live==1 and ln>3:
                    l[i][j]=0
                elif live==1 and ln<2:
                    l[i][j]=0
                if live==0 and ln==3:
                    l[i][j]=1
                j+=1
            i+=1
        i = 0
        while i<len(l):
            board[i]=l[i]
            i+=1
                
