class Solution:
    
    def c(self, n):
        f = []
        
        if n%2==0:
            return False
        for i in range(3,int(n**.5)+1,2):
            if n%i==0:
                return False
        return True
        
        
    def primePalindrome(self, N: int) -> int:
        
        if N<12:
            if N<=2:return 2
            if N<=3:return 3
            if N<=5:return 5
            if N<=7:return 7
            if N<=11:return 11
        
        tmp = len(str(N))//2
        
        start = 10**tmp
        
        while 1!=-1:
            s = str(start)
            
            s1 = int(s+s[::-1])
            s2 = int(s+s[:-1][::-1])
            
            num = min([s1,s2])
            if num>=N and self.c(num)==True:
                return num
            start+=1
