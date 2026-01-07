class Solution:
    def largeGroupPositions(self, S: str) -> List[List[int]]:
        final = []
        i = 0
        while i<len(S):
            j = i
            while j<len(S):
                if S[j]!=S[i]:
                    break
                j+=1
        
            if j-i>=3:
                final.append([i,j-1])
                
                i+=j-i
            else:
                i+=1
        return final
