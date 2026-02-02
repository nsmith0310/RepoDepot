class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        S = list(s)
        T = list(t)
        
        l = [0]
        m = [0]
        i = 0
        while i<len(S):
            try:
                ind = -1
                j = T.index(S[i])
                if j>=l[-1]:
                    l.append(j)
                    m.append(j)
                    del T[j]
                else:
                    while j<len(T):
                        if j>=l[-1] and T[j]==S[i]:
                            ind = j
                            break
                        j+=1
                    if ind ==-1:
                        return False
                    else:
                        l.append(ind)
                        m.append(ind)
                        del T[ind]
            except:
                return False
            i+=1
        print(l)
        m.sort()
        return m==l
