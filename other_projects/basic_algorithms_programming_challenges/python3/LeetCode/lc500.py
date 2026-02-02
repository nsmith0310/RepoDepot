class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        r1 = ["q","w","e","r","t","y","u","i","o","p"]
        r2 = ["a","s","d","f","g","h","j","k","l"]
        r3 = ["z","x","c","v","b","n","m"]
        l1 = []
        l2 = []
        for x in words:
            c = 0
            for y in r1:
                if y in x:
                    c+=1
                    break
            for y in r2:
                if y in x:
                    c+=1
                    break
            for y in r3:
                if y in x:
                    c+=1
                    break
            l1.append([x,c])
        for x in l1:
            if x[1]==1:
                l2.append(x[0])
        return l2
