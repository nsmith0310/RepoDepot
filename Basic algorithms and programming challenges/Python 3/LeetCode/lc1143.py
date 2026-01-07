class Solution:
    def __init__(self):
        self.tab = []
    
    def r(self,s1,s2,lim1,lim2):
        
        if lim1!=0 and lim2!=0:
       
        
            if self.tab[lim1-1][lim2-1]!=0:
                return self.tab[lim1-1][lim2-1]
        
            c=0
        
        
            if s1[-1]!=s2[-1]:
                
                c+=max([self.r(s1[:-1],s2,lim1-1,lim2),self.r(s1,s2[:-1],lim1,lim2-1)])
            else:
                c+=1+self.r(s1[:-1],s2[:-1],lim1-1,lim2-1)
        
            self.tab[lim1-1][lim2-1]=c
            return c
        else:
            return 0
                
                
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        lim1 = len(text1)
        lim2 = len(text2)
        
        self.tab = [[0 for i in range(0,lim2)] for j in range(0,lim1)]
        
        return self.r(text1,text2,lim1,lim2)
                
        
        
        
        
            
