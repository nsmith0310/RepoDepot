class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        l = set()
        
        
        i = 0
        while i<len(words):
            j = 0
            while j<len(words):
                if j!=i and words[i] in words[j]:l.add(words[i])
                j+=1
            i+=1
        return list(l)
