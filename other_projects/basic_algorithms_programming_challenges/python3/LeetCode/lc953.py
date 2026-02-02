class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        
        i = 0
        while i<len(words)-1:
            j = i+1
            while j<len(words):
                
                ind1 = ""
                ind2 = ""
                word1=words[i]
                word2=words[j]
                k = 0
                while k<len(word1) and k<len(word2):
                    pos1 = order.index(word1[k])
                    pos2 = order.index(word2[k])
                    ind1+=str(pos1)
                    ind2+=str(pos2)
                    if pos1<pos2:
                        
                        break
                        
                    elif pos2==pos1:pass
                    
                    else:
                        return False
                        
                    k+=1
                if ind1==ind2 and len(word1)>len(word2):
                    return False
                j+=1
            i+=1
        return True
                
