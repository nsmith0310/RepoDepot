class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        l = emails
        l2=[]
        
        for x in l:
            tmp = x[x.index('@'):]
            s = x[:x.index('@')]
            if '+' in s:
                t = s[:s.index('+')]
            else:
                t=s
            if '.' in t:
                u = t.replace('.','')
            else:
                u = t
            l2.append(u+tmp)
        return len(list(set(l2)))
