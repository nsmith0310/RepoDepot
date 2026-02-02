class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        
        
        l1 = list(map(int,date1.split("-")))
        l2 = list(map(int,date2.split("-")))
        
        
        start = []
        end  = []
        
        
        if l1[0]<l2[0]:
            start = l1
            end = l2
        elif l1[0]>l2[0]:
            start = l2
            end = l1
        elif l1[0]==l2[0]:
            if l1[1]<l2[1]:
                start = l1
                end  = l2
            elif l1[1]>l2[1]:
                start = l2
                end = l1
            else:
                if l1[2]<l2[2]:
                    start = l1
                    end = l2
                elif l1[2]>l2[2]:
                    start = l2
                    end = l1
                else:
                    return 0
        t = 0
        leap = [31,29,31,30,31,30,31,31,30,31,30,31,0]
        non = [31,28,31,30,31,30,31,31,30,31,30,31,0]
        
        if start[0]<end[0]:
            if start[0]%4!=0 or start[0]%4==0 and (start[0]%100 ==0 and start[0]%400!=0):
                t+=sum(non[start[1]:])
                t+=non[start[1]-1]-start[2]
            else:
                t+=sum(leap[start[1]:])
                t+=leap[start[1]-1]-start[2]
        
        
            start[0]+=1
            if start[0]<end[0]:
                while start[0]<end[0]:
                    if start[0]%4!=0 or start[0]%4==0 and (start[0]%100 ==0 and start[0]%400!=0):
                        t+=365
                    else:
                        t+=366
                    start[0]+=1
            t+=1
            
            start[1]=1
            start[2]=1
        
        if start[1]<end[1]:
            while start[1]<end[1]:
                if start[0]%4!=0 or start[0]%4==0 and (start[0]%100 ==0 and start[0]%400!=0):
                    t+=non[start[1]-1]
                else:
                    t+=leap[start[1]-1]
                start[1]+=1
        
        if start[2]<end[2]:
            t+=end[2]-start[2]
        
        return t
                    
            
            
        
        
