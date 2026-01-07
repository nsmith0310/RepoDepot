class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        mas = ["!","1","@","2","#","3","$","4","%","5","^","6","&","7","*","8","(","9",")","0","_","-","+","=","~","`","}","]","{","[","'","?","/",",","<",".",">","|",";",":"]
        l = list(set(list(S)))
        l4=[]
                
        banned=[0 for i in range(0,len(S))]
        non=""        
        
        for x in l:
            if x in mas:
                l4.append(x)
        s2=""
        i = 0
        while i<len(S):
            if S[i] in l4:
                banned[i]=S[i]
            else:
                non+=S[i]
            i+=1
        i = 0
        
        non=non[::-1]
        i = 0
        while i<len(non):
            j = 0
            while j<len(banned):
                if banned[j]==0:
                    banned[j]=non[i]
                    break
                j+=1
            i+=1
        return ''.join(banned)
        
        
                
                
