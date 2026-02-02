from copy import copy
class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        
        lim = len(S)
        nums = []
        
        
        while S!="":
            start = S[0]
            j = len(S)-1
            while j>=0:
                if S[j]==start:
                    break
                j-=1
            if j==len(S)-1:
                nums.append(len(S))
                break
            else:
                mx = 0
                s = set(list(S[:j+1]))
                tmp = list(s)
                
                ###print(tmp)
                for x in tmp:
                    ind = S.index(x)
                    start = S[ind]
                    j = len(S)-1
                    while j>=0:
                        if S[j]==start:
                            tmp3 = list(set(S[ind:j]))
                            for y in tmp3:
                                if y not in tmp:
                                    tmp.append(y)
                            
                            break
                        j-=1
                    if j>mx:
                        mx=j
                        print(mx)
                nums.append(len(S[:mx+1]))
                ###print(nums)
                S=S[mx+1:]
        return nums
