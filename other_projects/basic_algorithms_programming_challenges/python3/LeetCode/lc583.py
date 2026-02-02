class Solution:
    
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
    def minDistance(self, word1: str, word2: str) -> int:
        lim1 = len(word1)
        lim2 = len(word2)
        
        if lim1<=lim2:
            self.tab = [[0 for i in range(0,lim2)] for j in range(0,lim1)]
            
        
            x = self.r(word1,word2,lim1,lim2)
            
        
            return (lim1-x+lim2-x)
        else:
            
            self.tab = [[0 for i in range(0,lim2)] for j in range(0,lim1)]
        
            x = self.r(word1,word2,lim1,lim2)
        
            
        
            return (lim1-x+lim2-x)
        
        
        
        
        
