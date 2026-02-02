class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        w = word
        if w[0].upper()==w[0]:
            if w.upper()==w:
                return True
            if w[1:].lower()==w[1:]:
                return True
            else:
                return False
        i = 0
        while i<len(w):
            if w[i].upper()==w[i]:
                return False
            i+=1
        return True
