class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dic = []
        self.size = []
        

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        l = len(word)
        if l in self.size:
            i = 0
            while i<len(self.dic):
                
                if l==self.dic[i][0]:
                    self.dic[i][1].append(word)
                    break
                i+=1
        else:
            self.size.append(l)
            self.dic.append([l,[word]])
            self.size.sort()
            self.dic.sort(key=lambda x: x[0])
                    
            

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        l = len(word)
        try:
            ind = self.size.index(l)
            
            i = 0
            while i<len(self.dic[ind][1]):
                t = 0
                j = 0
                while j<len(word):
                    if word[j]!=self.dic[ind][1][i][j] and word[j]!=".":
                        t = 1
                        break
                    j+=1
                if t==0:
                    return True
                i+=1
            return False
            
            
        except:
            return False
            
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
