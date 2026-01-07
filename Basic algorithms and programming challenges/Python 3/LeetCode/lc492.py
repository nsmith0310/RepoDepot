class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        n = area
        f = []
        s = int(area**.5)
        while n%2==0:
            f.append(2)
            n//=2
        for i in range(3,s+1,2):
            if n%i==0:
                while n%i==0:
                    f.append(i)
                    n//=i
        if n>2:
            f.append(n)
        
        if len(f)==1:
            return [area,1]
        else:
            k = s
            while area%k!=0:
                k-=1
            l = [k,area//k]
            l.sort(reverse=True)
            return l
            
            
        
