class Codec:

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        
        l = longUrl.split("/")
        l.append(1)
        return l
        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        l = shortUrl
        
        tmp = l[-1]
        del l[-1]
        s=l[0]+"//"
        i = 2
        while i<len(l):
            s+=l[i]+"/"
            i+=1
        
        return s[:-1]
    
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
