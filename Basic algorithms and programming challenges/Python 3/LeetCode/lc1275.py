class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        r = [['U','U','U'],['U','U','U'],['U','U','U']]
        l = moves
        i = 0
        while i<len(l):
            if i%2==0:
                r[l[i][0]][l[i][1]]='X'
            else:
                r[l[i][0]][l[i][1]]='O'
            i+=1
        
        i = 0
        if ['X','X','X'] in r:
            return 'A'
        elif ['O','O','O'] in r:
            return 'B'
        elif r[0][0]=='X' and r[1][1]=='X' and r[2][2]=='X':
            return 'A'
        elif r[0][0]=='O' and r[1][1]=='O' and r[2][2]=='O':
            return 'B'
        elif r[0][2]=='X' and r[1][1]=='X' and r[2][0]=='X':
            return 'A'
        elif r[0][2]=='O' and r[1][1]=='O' and r[2][0]=='O':
            return 'B'
        elif r[0][0]=='X' and r[1][0]=='X' and r[2][0]=='X':
            return 'A'
        elif r[0][0]=='O' and r[1][0]=='O' and r[2][0]=='O':
            return 'B'
        elif r[0][1]=='X' and r[1][1]=='X' and r[2][1]=='X':
            return 'A'
        elif r[0][1]=='O' and r[1][1]=='O' and r[2][1]=='O':
            return 'B'
        elif r[0][2]=='X' and r[1][2]=='X' and r[2][2]=='X':
            return 'A'
        elif r[0][2]=='O' and r[1][2]=='O' and r[2][2]=='O':
            return 'B'
        
        for x in r:
            if 'U' in x:
                return 'Pending'
        return 'Draw'
