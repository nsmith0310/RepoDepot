class Solution:
    def judgeCircle(self, moves: str) -> bool:
        s = [0,0]
        i = 0
        while i<len(moves):
            if moves[i]=="L":
                s[0]-=1
            elif moves[i]=="R":
                s[0]+=1
            elif moves[i]=="D":
                s[1]-=1
            elif moves[i]=="U":
                s[1]+=1
            i+=1
        return s==[0,0]
