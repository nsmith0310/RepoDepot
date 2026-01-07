class Solution:
    def dayOfYear(self, date: str) -> int:
        l = list(map(int,date.split("-")))
        
        if l[0]%4!=0 or l[0]%4==0 and (l[0]%100 ==0 and l[0]%400!=0):
            m = [31,28,31,30,31,30,31,31,30,31,30,31]
            t = 0
            i = 1
            while i<l[1]:
                t+=m[i-1]
                i+=1
            return t+l[2]
        else:
            m = [31,29,31,30,31,30,31,31,30,31,30,31]
            t = 0
            i = 1
            while i<l[1]:
                t+=m[i-1]
                i+=1
            return t+l[2]
