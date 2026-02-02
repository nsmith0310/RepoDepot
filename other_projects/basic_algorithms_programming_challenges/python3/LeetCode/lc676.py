class MagicDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = dict()

    def buildDict(self, dict: List[str]) -> None:
        """
        Build a dictionary through a list of words
        """
        for x in dict:
            try:
                self.d[len(x)].append(x)
            except:
                self.d[len(x)] = [x]
        
    def search(self, word: str) -> bool:
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        """
        
        try:
            for x in self.d[len(word)]:
                ###print(x)
                c = 0
                i = 0
                while i<len(x):
                    if x[i]!=word[i]:
                        c+=1
                        if c>1:
                            break
                    i+=1
                ###print(c)
                if c==1:
                    return True
            return False
        except:
            return False
        


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dict)
# param_2 = obj.search(word)
