class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        
        self.lim = len(persons)
        self.ti = []
        
        d = dict()
        mx = 0
        
        mx_val = 0
        self.w = []
        i = 0
        mx = 0
        while i<self.lim:
            if i!=self.lim-1:
                self.ti.append([times[i],times[i+1]-1])
            
            try:
                d[persons[i]]+=1
                if d[persons[i]]>=mx:
                    mx = d[persons[i]]
                    mx_val = persons[i]
                    self.w.append(persons[i])
                else:
                    self.w.append(mx_val)
            except:
                d[persons[i]]=1
                if d[persons[i]]>=mx:
                    mx = d[persons[i]]
                    mx_val = persons[i]
                    self.w.append(persons[i])
                else:
                    self.w.append(mx_val)
                
            
            i+=1
        self.ti.append([times[-1],10000000000])
        
    def q(self, t: int) -> int:
        l = 0
        h = self.lim-1
        m = (l+h)//2
        
        while l<=h:
            if t>=self.ti[m][0] and t<=self.ti[m][1]:
                return self.w[m]
            elif t<self.ti[m][0]:
                h = m-1
                m = (l+h)//2
            else:
                l = m+1
                m = (l+h)//2


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)
